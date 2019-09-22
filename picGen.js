const puppeteer = require('puppeteer');

(async () =>
{
  const browser = await puppeteer.launch(
    {
      defaultViewport
      {
        width: 500,
        height: 800,
        islandscape: true
      }
    }
  );

  const page = await browser.newPage();

  await page.goto(
    mailto:name@domain
    {
      waitUntil: 'networkIdle2'
    }
  );

  await page.screenshot({omitBackground: true});

  await browser.close();
})
