# Database Diagram

https://dbdiagram.io/d/5f5f875f7da1ea736e2dccf7

# Landing Sites/Pages/? (No idea what to call this)

Name                | Description 
------------------  | ----------  
Home                | The home page for Dan's bagels 
Login               | Login page 
Create Account      | New user account creation page  
Menu                | List of all current menu items 
Order Customization | Page for adding toppings/drinks/etc. to bagels 
Bagel Bag           | Shopping cart for bagels. I've never put bagels in a shopping cart though 
Checkout            | Payment and such 
Order Tracking      | Order Tracking Page (read Domino's Pizza Tracker ripoff)
Profile             | User account information page
Profile Management  | Page for changing account information
Employee Portal     | Home page for employess
Chef                | Page/Tab for chef to do chef things
Cashier             | Page/Tab for cashier to do cashier things
Owner               | Page/Tab for owner to do owner things
Reports             | Page for owner to view reports
Inventory           | Page for all inventory management. Rendering of this page will be dependent upon user authentication


# API Specification (Not really API Specification, but similar thing. Someone please help me give things good names)
Page                | URL                           | Notes/Description (if not self-explanatory)
------------------- | ----------------------------- | -------------
Home                | /                             | 
Accounts            | /accounts                     | Internal endpoint for CRUDding account info
Login               | /accounts/login               | 
Create Account      | /accounts/create              | 
Password reset      | /accounts/reset-password      | Page for resetting account password
Profile             | /accounts/view                | 
Profile Management  | /accounts/edit                |
Menu                | /menu                         | 
Order Customization | /menu/\<item-id\>/customize   | 
Bagel Bag           | /bagel-bag                    |
Pizza Tracker       | /tracking                     | 
Orders              | /orders/\<order\_id\>         | Our internal endpoint for CRUDding order data 
Checkout            | /bagelbag/place-order         | 
Employee Portal     | /employee                     | 
Chef                | /employee/chef                | See note below  
Cashier             | /employee/cashier             | See note below 
Owner               | /employee/owner               | These won't necessarily be pages by themselves, but I think the organization will be better if each role can have its own endpoint
Reports             | /employee/owner/reports       |  
Inventory           | /employee/inventory-management| 

