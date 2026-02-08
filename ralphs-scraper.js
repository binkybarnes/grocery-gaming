function getClassList(el) {
  return [...el.classList].filter(c => !/\d/.test(c));
}

function hasAllClasses(el, classes) {
  return classes.every(c => el.classList.contains(c));
}

function detectRows(container) {
  const children = [...container.children];

  const classFreq = {};
  for (const child of children) {
    for (const cls of getClassList(child)) {
      classFreq[cls] = (classFreq[cls] || 0) + 1;
    }
  }

  const threshold = Math.max(1, Math.floor(children.length / 2) - 2);
  const commonClasses = Object.keys(classFreq).filter(
    cls => classFreq[cls] >= threshold
  );

  return children.filter(el =>
    commonClasses.some(cls => el.classList.contains(cls))
  );
}

function getTextOnly(el) {
  return el.cloneNode(true).textContent.trim();
}

function extractRowData(row) {
  const data = {};

  function walk(node, path = "") {
    for (const child of node.children) {
      const classes = [...child.classList].map(c => `.${c}`).join("");
      const newPath = `${path}/${child.tagName.toLowerCase()}${classes}`;

      const text = child.textContent.trim();
      if (text) data[newPath] = text;

      if (child.href) data[`${newPath}:href`] = child.href;
      if (child.src) data[`${newPath}:src`] = child.src;

      walk(child, newPath);
    }
  }

  walk(row);
  return data;
}


function scrapeTable(container) {
  const rows = detectRows(container);
  return rows.map(extractRowData);
}

const { chromium } = require("playwright-extra");
const StealthPlugin = require("puppeteer-extra-plugin-stealth");

chromium.use(StealthPlugin());

(async () => {
  // 1. Launch with standard evasion
  const browser = await chromium.launch({ headless: false });
  
  // 2. Use a persistent-style context with a real user agent
  const context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
  });

  // 3. NUCLEAR OPTION: Nuke the webdriver flag before the page loads
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });

  const page = await context.newPage();

  // 4. THE INTERCEPTOR: Listen for the JSON data response
  page.on('response', async (response) => {
    // Ralphs' internal search API usually includes this string
    if (response.url().includes('/api/v1/search') && response.status() === 200) {
      try {
        const data = await response.json();
        console.log("--- MILK DATA FOUND ---");
        
        // Loop through the first few products and log prices
        const products = data.products || [];
        products.slice(0, 5).forEach(p => {
          console.log(`${p.brand} ${p.description}: $${p.price.regular}`);
        });
      } catch (e) {
        // Ignore responses that aren't valid JSON
      }
    }
  });

  console.log("Navigating to Ralphs...");
  
  // 5. Navigate to the search page
  await page.goto("https://www.ralphs.com/search?query=milk", {
    waitUntil: "domcontentloaded",
  });

  // Keep it open for a few seconds to ensure the API call finishes
  await page.waitForTimeout(50000);
  
  await browser.close();
})();