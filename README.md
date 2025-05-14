# Imperative Care Multi-Site WordPress Project

## Overview
A custom built WordPress multisite for Imperative Care, built using modern development practices and deployed on WP Engine which uses IC theme as a primary theme. The project is structured to handle multiple WordPress sites within a single installation.


## Theme Information
The project uses a custom theme (Imperative Care Theme) built on top of Sage, which includes:
- Genesis Block Theme
- Imperative Care Theme


### Dependencies
- Node.js packages:
  - Bootstrap 4.5.2
  - jQuery 3.5.1
  - Laravel Mix for asset compilation
  - Various UI components (Fancybox, AOS, Bootstrap Select)
  - Development tools (ESLint, Stylelint)

## Table of Contents
- [Environments](#environments)
- [Prerequisites](#prerequisites)
- [Server](#server)
- [Project Setup](#project-setup)
- [Maintenance Tasks](#maintenance-tasks)
- [Regular Testing](#regular-testing)
- [Theme Development](#theme-development)



## Environments
- Dev
- Stage
- Prod URL: https://imperativecare.com/

## Prerequisites
- PHP 7.2.5 or higher (curerently using PHP 7.4.30)
- Node.js for frontend asset compilation ( version: >= 12.0.0 (we are currently using 14.\* lts))
- Composer for PHP dependencies
- Wordpress >= 6.8
- PHP >= 7.4.30 (with php-mbstring enabled)
- Yarn: Package manager
## Server

- WP Engine



## Project Setup 
1. Clone files from remote repository
2. Import the database
3.  Download the Uploads folder and place it in the wp-content folder
4. Update the following database tables:
   - `wp_options` → Update local site URL (no trailing slash - '/' at the end)
   - `wp_site` → Replace domain with `impcare.local` (or your local domain)
   - `wp_blogs` → Replace site URL with `impcare.local`
5. Update user records if necessary
6. Use the correct Node version:
   ```bash
   nvm use 14

## Theme Development
- Go to the theme directory 
`cd wp-content/themes/ic`
- Install PHP dependencies
`composer install`
- Install other dependencies
`yarn`
- Building assets like Javascript and CSS
`yarn build`
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

