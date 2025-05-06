# Imperative Care

## Environments
* Dev URL:  https://impcaredev.wpengine.com/  
* Stage URL:https://impcarestage.wpengine.com/ 
* Prod URL: https://imperativecare.com/

## Prerequisites

* Wordpress >= 6.8
* PHP >= 7.4.30 (with php-mbstring enabled)
* Composer
* Node.js version: >= 12.0.0 (we are currently using 14.\* lts)
* Yarn: Package manager

## SERVER

- WP Engine

## Project Setup Process
* Clone files from remote repository
* Import db
* wp_option >> local site URL (but no '/' at the end)
    all wp_option (there are wp_option2, wp_option3, wp_option4,.....)
* wp_site (just keep domain name "impcare.local")
    [note: impcare.local should be replaced with your site domain]
* wp_blogs (replace site URL with "impcare.local")
    [note: impcare.local should be replaced with your site domain]
* user update
* nvm use 14
* yarn
* yarn build
* make a "cache" folder wp-content >> uploads >> under sites >> 3
* make a "cache" folder wp-content >> uploads >> under sites >> 4
* make a "cache" folder wp-content >> uploads >> under sites >> 5
    
    
## Regular Maintainenance Tasks
* Plugins updates
* PHP update
* WP core update
* Any security update
* Security audit using https://sitecheck.sucuri.net/ 
* Any minor fixes introduced by update* s
* Update backend credentials for Admin Console every three months. Only update credentials for the Outside user (this could be sujan@ruca.co, sujan@outside.tech, etc.)
* Add ACF license key in all environments if not present
* HTTP to HTTPS redirection check
* Check for robot.txt and sitemap.xml
* Need to create an empty cache folder inside uploads folder if issue of Acorn arises.

## Regular Tests to be carried out
* Regression testingnd it to me asap. should be performed in the whole website
* Sanity test the CMS
* Test Contact forms
* Edit / create pages and perform regression testing
* HTTP to HTTPS redirection check
* check for robot.txt and sitemap.xml
* Test User enumeration
* When you post the website on LinkedIn, the OG image and OG title are not the same as what you post on Facebook. It should be the same as OG image and OG Title for Facebook.

## Backups 
* WP Engine performs automated daily backups
* Up to 40 backup points are available in the User Portal
* We have triggered a manual backup for the current stable version.

    Backup Info,Description,ID,Latest Backup
    April Maintenance -- created by: sujan@mediacause.org,1745216483,Apr 21, 2025, 12:07 PM

