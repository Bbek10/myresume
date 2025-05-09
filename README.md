# Imperative Care
A custom WordPress multisite implementation for Imperative Care, built using modern development practices and deployed on WP Engine.

## Table of Contents
- [Environments](#environments)
- [Prerequisites](#prerequisites)
- [Server](#server)
- [Project Setup](#project-setup)
- [Maintenance Tasks](#maintenance-tasks)
- [Regular Testing](#regular-testing)
- [Backups](#backups)


## Environments
- Dev URL:  https://impcaredev.wpengine.com/  
- Stage URL:https://impcarestage.wpengine.com/ 
- Prod URL: https://imperativecare.com/

## Prerequisites

- Wordpress >= 6.8
- PHP >= 7.4.30 (with php-mbstring enabled)
- Composer
- Node.js version: >= 12.0.0 (we are currently using 14.\* lts)
- Yarn: Package manager

## Server

- WP Engine

## Project Setup 
1. Clone files from remote repository
2. Import the database
3. Update the following database tables:
   - `wp_options` → Update local site URL (no trailing slash - '/' at the end))
   - `wp_site` → Replace domain with `impcare.local` (or your local domain)
   - `wp_blogs` → Replace site URL with `impcare.local`
4. Update user records if necessary
5. Use the correct Node version:
   ```bash
   nvm use 14
- user update
- Install dependencies
-    yarn
-    yarn build

- Create cache folders under:
    - make a "cache" folder wp-content >> uploads >> under sites >> 3
    - make a "cache" folder wp-content >> uploads >> under sites >> 4
    - make a "cache" folder wp-content >> uploads >> under sites >> 5
    
    
##  Maintenance Tasks
- Update plugins, PHP version, and WordPress core
- Perform regular security audits ([Sucuri SiteCheck](https://sitecheck.sucuri.net/))
- Apply any necessary security patches or fixes
- Update backend credentials for Admin Console every three months.
- Add ACF license key in all environments if not present
- Confirm HTTP to HTTPS redirection is functioning
- Validate presence of `robots.txt` and `sitemap.xml`
- Recreate empty cache folders if Acorn-related errors occur

## Regular Testing

- Full regression testing across the website
- CMS sanity checks
- Test all contact forms
- Verify ability to create/edit pages
- Confirm consistent OG image and title across platforms (LinkedIn, Facebook)
- Test HTTP to HTTPS redirection
- Verify robots.txt and sitemap.xml
- Run user enumeration security tests
- When you post the website on LinkedIn, the OG image and OG title are not the same as what you post on Facebook. It should be the same as OG image and OG Title for Facebook.

## Backups

- WP Engine provides automated daily backups
- Up to 40 backup points available in the User Portal
- Manual backups are triggered before major updates or deployments

| Description       | Created By                 | ID         | Latest Backup        |
|-------------------|----------------------------|------------|----------------------|
| April Maintenance | sujan@mediacause.org       | 1745216483 | Apr 21, 2025, 12:07 PM |
