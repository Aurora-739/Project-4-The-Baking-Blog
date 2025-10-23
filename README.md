# Project-4-a- : The Food Blog

The Baking Blog is an engaging online platform designed to inspire and guide baking enthusiasts of all skill levels. The site offers detailed baking recipes, complete with step-by-step instructions, ingredient lists, and recommended cooking utensils, making it easy for users to follow along and create delicious baked goods at home. Targeted at home bakers, hobbyists, and anyone passionate about baking, The Baking Blog aims to be a go-to resource for discovering new recipes and sharing baking experiences.

With features such as user authentication, commenting, and an intuitive design, The Baking Blog encourages a community-driven environment where users can leave feedback, ask questions, and engage with other bakers. This platform will be useful for its target audience by providing reliable, easy-to-follow recipes, fostering interaction, and helping bakers improve their skills while connecting with like-minded individuals.

![image](https://github.com/user-attachments/assets/63ef5193-04c9-4789-a251-e03df76aaaa1)
laptop

![image](https://github.com/user-attachments/assets/0d98dc63-0ad1-4bc4-9a2e-946ec61a7c2f)
ipad
![image](https://github.com/user-attachments/assets/ca8cc73e-2f5a-4142-a8fd-cdecd84edf52)
iphone

deployed link: https://food-blog-app-8f681c0f0074.herokuapp.com/

## Existing Features
### Navigation Bar
The navigation bar appears on all pages, providing easy access to the Home page, user authentication links (login, logout, register), and the blog’s main sections. This consistent navigation allows users to move effortlessly through the site on any device, enhancing usability and engagement.
![image](https://github.com/user-attachments/assets/1d2eed2b-0857-4e24-9aff-9e12937140c7)
pre login

![image](https://github.com/user-attachments/assets/5b1d3bf4-84f1-4196-9dd0-1f06fc057d23)
post login


### Home Page with Recipes
The home page shows a list of baking posts with pictures and titles. It’s paginated, so users can browse through recipes easily and pick the ones they want to check out.

![image](https://github.com/user-attachments/assets/79efffe0-0150-4318-ada9-f65e10a2e881)


### Recipe Detail Page
On each recipe page, users see all the details like the utensils, ingredients, and step-by-step instructions. There’s also a big picture and info about the author. Plus, users who are logged in can leave comments, making it more interactive.

![image](https://github.com/user-attachments/assets/5aa85b40-326d-42ae-b60e-5843d002ef49)


### User Login and Signup
Users can create accounts, log in, and log out. Once logged in, they can comment on recipes and even edit or delete their own comments. This keeps the community active and secure.

![image](https://github.com/user-attachments/assets/4fcf5304-3af7-4a63-a830-ba3c480db324)
![image](https://github.com/user-attachments/assets/9796f318-6d47-4d5e-a7e4-a3c672414f72)
![image](https://github.com/user-attachments/assets/ada5306d-9b22-42fa-bd2a-26708868ac58)
   
### Comments System
Users can leave comments on recipes, but comments need approval before showing up to keep things nice. Users can also edit or delete their own comments, so they stay in control of what they say.
went through each blog post manually & tested comments & buttons (i know this isn't the most effiecient way to do it, however there are not many blog posts currently)
![image](https://github.com/user-attachments/assets/b4378217-c9b8-4e2d-ae05-93b91600d8a5)
![image](https://github.com/user-attachments/assets/620b2c59-d61e-4e1e-aed6-d8e1af1d9ccb)
![image](https://github.com/user-attachments/assets/da081e02-3baa-404e-94d1-b0c8ad2eef97)


### Responsive Design
The whole site works well on phones, tablets, and computers. No matter what device you use, the site looks good and is easy to use.(shown prev.)

## The Design Process

I chose to build a website that allows users to view blog posts created by the admin. Users can also submit comments on blog posts, which can be approved or deleted by the admin. 
The main goal in the creation of this website was to create a positive warm environment for people to come to for baking ideas and to share their own experiences with the recipe's maybe even give some at home hacks if they have any.

I chose soft colours and a rounded design to create a bubbly and warm environment, aiming to make the page seem like a safe place where users can comment and share ideas.

The app structure was planned around CRUD functionality — allowing users to create, view, update, and delete comments.

### Overview 
The process began with a quick sketch out of a wireframe. I chose to do my sketches on canva because it's quick and easy, I simply used square shapes to mark out the approximate location of what I wanted the end result to look like. Although the website doesn't look exactly the same as the wireframe, it was an easy base for me to refer back to during the development process.

blog page: <img width="978" height="540" alt="image" src="https://github.com/user-attachments/assets/e551dddd-fdbb-4e55-af50-b14bd1186a3c" />
item page: <img width="960" height="539" alt="image" src="https://github.com/user-attachments/assets/1991fa06-d22e-4950-b6c4-8698b8764121" />
home page: <img width="959" height="543" alt="image" src="https://github.com/user-attachments/assets/3540c8ba-cc04-46d9-a5b2-3dccea5af20e" />

After my wireframes were drawn up I tried out a few different colours. In my origional design (as you can see above) I chose a bright colour scheme, primarily including orange and yellow.

<img width="968" height="555" alt="image" src="https://github.com/user-attachments/assets/58c6e9c4-4239-4b77-a513-5f1f552181ec" />

After my work had been marked it was noted that this colour scheme was not particularly UI friendly, although I included a hover feature which did aid in UI as it changed the colours from yellow and red to turquiose and red. I have thus made the switch from the almost monochromatic palette to a colour palette mainly consisting of pink and green, the colours on the opposite sides of the colour wheel as well as the difference in shades, should make the page more UI friendly for those with visual impairments or simply those who wish to view the site more easily at a glance.

<img width="1310" height="754" alt="image" src="https://github.com/user-attachments/assets/87e5ed8c-4fc1-4070-81bd-bedc7d4f6a94" />

### Typography:
“Poppins” for headers and “Lato” for body text to maintain readability.

### Layout:
Recipes displayed in cards for easy scanning, inspired by Pinterest-style grids.

### UX Decisions: 
Navigation kept simple (Home, Add Recipe, Login) to reduce clutter.

## CRUD Functionality

Create: Users can create new comments. (these comments can then be chosen to be displayed by the admin - I chose to include this feature as I wanted the blog to be a safe place so manual filtering of comments would help in there not being any super negativity or rudeness which can often be found on blogs / other social media.)
<img width="1239" height="696" alt="image" src="https://github.com/user-attachments/assets/16a94e7e-0694-4013-89b8-5906f3ce1d0c" /> (e.g. of an unnapproved comment in the admin section).

Read: All comments are displayed on the recipe's page and can be easily viewed.

Update: Logged-in users can edit their own comments.

Delete: Users can delete comments they created.
This makes the app fully dynamic and interactive, rather than static.

## Testing
For this project, I did a lot of manual testing across all of the main features to make sure the site works as expected and gives users the experience I designed for.

### Manual Testing
I tested the following:

### Navigation Bar:
* Checked all navigation links (Home, Login, Register, Logout) to make sure they route correctly and work whether the user is logged in or not.

### Post List (Home Page):
* Made sure that all posts display properly with their images, titles, and authors. I clicked each post to check that it links to the correct post detail page.

### Post Detail Page:
* Checked that all the post details display (title, author, date, utensils, ingredients, and steps).
* Tested leaving a comment when logged in, making sure it saves and appears. Also checked that when I leave a comment, it shows as awaiting approval until I approve it manually.

### Comment Edit/Delete Buttons:
* Made sure that only the comment author can see and use the Edit and Delete buttons.
* Tested editing a comment and checked that the new text saves.
* Tested the Delete button and the confirmation modal to make sure the comment is fully deleted from the database and disappears from the post page.

### User Authentication (Signup/Login/Logout):
* Tested registering a new account.
* Made sure login works with correct credentials and shows the correct user messages.
* Tested logging out and being redirected as expected.

### Pagination:
* For when there are more posts, I tested the next/previous buttons to make sure they work and the right posts load on each page.

### Social Media Links:
* Clicked all the footer social media links (Facebook, X/Twitter, Instagram) to make sure they open in a new tab and go to the right sites.

## Responsive Testing (Screen Sizes)
I tested the site on different devices and screen sizes:

### Mobile (iPhone SE and iPhone 13 using Chrome DevTools):
* Navigation bar collapses and works with mobile toggle.
* Images and text scale well without breaking layout.
* Forms for comments and signup stay readable and usable.

### Tablet (iPad):
* Layout scales nicely, two-column sections stack vertically.
* Cards and post previews adjust correctly.

### Desktop (Chrome and Firefox):
* Tested on a 1080p monitor and an ultrawide.
* Everything stayed centered and readable.
  
## Browser Compatibility Testing
Browsers I tested on:
* Google Chrome (Latest Version)
* Firefox (Latest Version)
* Microsoft Edge
Everything looked and worked the same across these.

## Validator Testing
### HTML:
Passed through the W3C Markup Validator.
No major errors came up. (a few warnings however, I deemed the code mentioned in the warnings to be too vital to remove or change).

### CSS:
Ran the stylesheet through the W3C Jigsaw CSS Validator.
Again, no errors found.

## Bugs Found and Fixed
### Modal Button IDs:
At first, the delete confirmation modal wasn’t picking up the correct comment ID when multiple comments were shown. I fixed this by making sure each button targets the right comment dynamically.

### Bootstrap Linking Error:
At first, the Bootstrap styles and scripts weren’t being applied properly across all pages. This caused layout issues with the navbar and modals, and some buttons didn’t look or behave as expected.
I realised I had linked to the wrong Bootstrap CDN version in my base template.
After updating the link to the correct Bootstrap 5 CDN and making sure both CSS and JS files were included in the right order, everything displayed and worked as expected.

## Unfixed Bugs
Currently, I don’t have any known unresolved bugs.
Everything works as expected across the features and devices I tested.

## Pep8 
(https://peps.python.org/pep-0008/)
I used the above link and read through my code - I did this manually so unfortunatly there aren't any particulary screenshots I can share with you but I have included screenshots of my code which I think display the pep8 test well.
- [x] Code Lay Out
<img width="692" height="320" alt="image" src="https://github.com/user-attachments/assets/31be1add-c43a-4ed1-b163-bf9266d5effe" />
- [x] String Quotes
- [x] White space in expressions & statements.
- [x] When To use trailing commas
- [x] Comments
- [x] Naming Conventions
<img width="717" height="361" alt="image" src="https://github.com/user-attachments/assets/4f0bbef1-b838-4d1c-8d08-25cc87be5619" />
- [x] Programming Recommendations
      - I believe these can change based on situation and so a single screenshot will not do this section justice.
- [x] References
- [x] Copywrite
      - Both are noted further in the README.md
## Credits
### Content
* The comment functionality (add, edit, delete, and approve) was guided by the Django tutorials and documentation from the official Django project site.
* I used the Code Institute Django Blog Walkthrough as a main reference for structuring my Django views and templates.(changes were made)
* The icons for the navigation and social media links came from Font Awesome.
* I followed tutorials from YouTube and Stack Overflow when I needed help with Bootstrap modals and Django form handling.

###  Media
* The placeholder images for blog posts came from Pexels, which offers free stock images.
* The default image shown when no featured image is uploaded is stored locally in my static files folder (static/images/default.jpg). I got this from free Image
* Any food-themed photos used in posts were from free-to-use, open-source image sites like free Image and Pexels.

### Extra Help
* I used Bootstrap 5 documentation for layout and responsiveness guidance.
* For form styling and formatting, I used django and css from the Code Institute's Blog Walkthrough as my base code (changes were made).
* Bug troubleshooting help came from questions and answers found on Stack Overflow.
* I used the W3C Validator and Jigsaw CSS Validator to check and fix my code.




