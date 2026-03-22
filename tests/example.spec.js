import { test, expect } from '@playwright/test';

test('Simple Form Demo Test', async ({ page }) => {
  await page.goto('https://www.testmuai.com/selenium-playground/');
  await page.getByRole('link', { name: 'Simple Form Demo' }).click();
  await expect(page).toHaveURL(/.*simple-form-demo/);
  const message = 'Welcome to TestMu AI';
  await page.fill('#user-message', message);
  await page.click('#showInput');
  await expect(page.locator('#message')).toHaveText(message);
});