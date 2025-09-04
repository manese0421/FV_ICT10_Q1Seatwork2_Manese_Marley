from pyscript import display, HTML # to make sure the code doesnt display <li></li> as text

museum_name = "Summertime Museums" # displays the museum name on the page
director_name = "Marley 'Summer' Manese" # string, contains my name (director name)
year_established = 2025 # integer, indicates year 
popular_ticket_price = 15.00 # ticket price for museum entrance
has_guided_tours = True # boolean,  indicates guided tours
exhibit_names = ["Impressionist Masterpieces", "Modern Sculpture", "Renaissance Treasures"] # list of strings, exhibit names
business_hours = 'Open 9 A.M - 10 A.M' # this is a string

ticket_prices = [ 
    {"type": "Adult", "price": 15.00},
    {"type": "Student", "price": 10.00},
    {"type": "Senior", "price": 12.00}, # dictionary, shows ticket prices for each age range
    {"type": "Child", "price": 8.00},
    {"type": "Member", "price": 0.00}
]

visitor_restrictions = ["No flash photography", "No food or drinks", "No touching artworks"] # list of strings, displays restrictions
tax_rate = 0.10 # this is a float

# displays on the page the variables' value :)
display(f"This is {museum_name}", target="about")
display(f"Founded by {director_name}", target="about")
display(f"Est. In {year_established}", target="about")
display(f"Popular Ticket Price: ₱{popular_ticket_price}", target="about")
display(f"Tours With Guide: {has_guided_tours}", target="about")
display(f"Open Hours: {business_hours}", target="about")
display(f"Current Tax Rate: {tax_rate}", target="about")

# styling exhibit section
for exhibit in exhibit_names:
    display(HTML(f"<li class='list-group-item'>{exhibit}</li>"), target="exhibits")

# styling ticket section 
for ticket in ticket_prices:
    display(HTML(f"<li class='list-group-item'>{ticket['type']} – ₱{ticket['price']:.2f}</li>"), target="tickets")

# styling restriction section
for rule in visitor_restrictions:
    display(HTML(f"<li class='list-group-item'>{rule}</li>"), target="rules")