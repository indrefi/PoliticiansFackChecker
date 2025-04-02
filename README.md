
# PoliticiansFactChecker - GitHub Pages Website Setup & Workflow

This repository hosts **factual_checker**, a Python application developed by **Florin Balint**, located in the **factual_checker** folder. 

The application analyzes public statements made by politicians, classifying them as True, False, or variations of truth based on the extracted information. The results are exported to a CSV file at **factual_checker/app/politician_stats.csv**.

To enhance usability, **Ionut Indre** extended the logic to present the exported data through interactive charts, making the insights more engaging and accessible to users. 
Additionally, automation has been implemented, with a scheduled job running factual_checker daily to update the CSV file automatically.

This repository contains all the logic to automatically update the CSV file daily using GitHub Actions and host a website using GitHub Pages.

---

## 1 Setup GitHub Actions Workflow

To automate the update of the `politician_stats.csv` file and host it on GitHub Pages, we need to create a GitHub Actions workflow.

### Create the Workflow
1. In your repository, create a folder `.github/workflows/` (if it doesn’t already exist).
2. Inside that folder, create a file `update_csv_job.yml` and add the following contents:

```yaml
name: Update CSV Daily

on:
  schedule:
    - cron: "0 0 * * *"  # Runs daily at midnight UTC
  workflow_dispatch:  # Allows manual trigger

jobs:
  update:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.x"

      - name: Install Dependencies
        run: |
          pip install --upgrade pip
          pip install -r factual_checker/requirements.txt

      - name: Run Python Script
        run: python factual_checker/app/main.py

      - name: Commit and Push Changes
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          git add factual_checker/app/politician_stats.csv
          git commit -m "Auto-update CSV [$(date)]" || echo "No changes to commit"
          git push
```

### Explanation:
- This workflow will:
  - Run **daily at midnight UTC** to update the CSV file (`politician_stats.csv`).
  - Install necessary Python dependencies from `factual_checker/requirements.txt`.
  - Run the Python script (`factual_checker/app/main.py`) to update the CSV.
  - Push the updated CSV file back to GitHub.

---

## 2 Workflow Permissions

### Allowing Write Permissions for GitHub Actions

To enable GitHub Actions to push changes (e.g., updating `politician_stats.csv`) back to your repository, you need to **set the appropriate permissions**.

#### Steps to Enable Write Permissions for GitHub Actions:
1. Go to your GitHub repository **Settings**.
2. In the left sidebar, click **"Actions" → "General"**.
3. Scroll down to **"Workflow permissions"**.
4. Select **"Read and write permissions"**.
5. Click **Save**.

This ensures that the GitHub Actions bot can commit and push changes back to the repository.

---

## 3 Enable GitHub Pages

To host your `index.html` file publicly, you need to enable **GitHub Pages**.

### Steps to Enable GitHub Pages:
1. Go to your repository **Settings**.
2. Scroll down to the **Pages** section.
3. Under **Source**, select **main** (or `master`, depending on your setup) as the branch and `/ (root)` as the folder.
4. Click **Save**.
5. Your site will now be publicly available at:
   ```
   https://yourusername.github.io/your-repo/
   ```

---

## 4 Check Website Status

Once your website is live, you can check its status:
1. Go to **Settings** → **Pages** to see the current deployment status.
2. You should see **"Your site is live"** after it finishes deploying.
3. If there are any issues, check the **Actions** tab for logs and debugging.

---

## 🎉 The Website is Live!

After completing these steps, the website is hosted on GitHub Pages and automatically updates daily. You can access it via:  
```
https://yourusername.github.io/your-repo/
```

---
