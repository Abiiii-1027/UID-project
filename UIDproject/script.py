import os

pages = [
    ("index.html", "Home"),
    ("login.html", "Login"),
    ("register.html", "Register"),
    ("dashboard.html", "Dashboard"),
    ("search.html", "Search Cruises"),
    ("itinerary.html", "Itinerary Planner"),
    ("activity.html", "Activity Selection"),
    ("food.html", "Food Options"),
    ("overview.html", "Cruise Overview"),
    ("cabins.html", "Cabin Selection"),
    ("help.html", "Help Center"),
    ("review.html", "Reviews"),
    ("rating.html", "Cruise Rating"),
    ("themed.html", "Themed Holidays"),
    ("payment.html", "Payment"),
    ("contact.html", "Contact Us"),
]

import random

# ---------- illustrations (generated SVGs; swap paths here to use real photos) ----------
IMG = {k: "images/%s.svg" % k for k in "hero goa caribbean med lakshadweep ship cabin food pool night".split()}
# sky top, sky bottom, sun, sea, features
SCENES = {
    "hero": ("#0a2a43", "#f2a65a", "#ffd27a", "#0b5a7a", "ship"),
    "goa": ("#ff9a62", "#ffe0a3", "#fff3c4", "#0f8b9c", "palms"),
    "caribbean": ("#2bb3e8", "#c9f1ff", "#fff7c2", "#0aa3b8", "island,ship"),
    "med": ("#4a90d9", "#fbd9b0", "#ffe9a8", "#14598a", "town"),
    "lakshadweep": ("#3ec6c1", "#eafff6", "#fffbd0", "#10a6ad", "palms,island"),
    "ship": ("#16324f", "#7fb7d8", "#e8f4ff", "#0a3350", "ship"),
    "cabin": ("#8fd3f4", "#e6f7ff", "#fff6bf", "#1d8fb5", "window"),
    "food": ("", "", "", "", "plate"),
    "pool": ("#ff7e5f", "#feb47b", "#fff0b3", "#0fb5c4", "pool"),
    "night": ("#0b1026", "#3a2a6b", "#e8e8ff", "#0d1b3d", "ship,stars"),
}


def palm(x, y, s):
    g = '<g transform="translate(%d %d) scale(%s)"><path d="M0 160Q20 80 60 0" stroke="#6b4a2b" stroke-width="9" fill="none"/>' % (x, y, s)
    g += "".join('<ellipse cx="45" rx="50" ry="10" fill="#1d8a4b" transform="translate(60 0) rotate(%d)"/>' % a for a in (-170, -130, -90, -50, -10, 30))
    return g + "</g>"


def scene(top, bot, sun, sea, ex):
    r = random.Random(top)
    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" preserveAspectRatio="xMidYMid slice"><defs>'
         '<linearGradient id="a" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>'
         '<linearGradient id="b" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="#052238"/></linearGradient></defs>' % (top, bot, sea)]
    if "plate" in ex:
        o.append('<rect width="800" height="500" fill="#f3dfbf"/><circle cx="400" cy="250" r="200" fill="#fff"/>'
                 '<circle cx="400" cy="250" r="155" fill="#fbefd9" stroke="#ead6b2" stroke-width="4"/>'
                 '<circle cx="360" cy="255" r="70" fill="#f7e8c0"/><circle cx="450" cy="230" r="58" fill="#c24e22"/>'
                 '<circle cx="455" cy="225" r="38" fill="#d9692f"/><ellipse cx="400" cy="335" rx="60" ry="20" fill="#4f9d4b"/>'
                 '<ellipse cx="330" cy="170" rx="28" ry="14" fill="#6bb85f"/><path d="M640 90a60 60 0 0 1 0 120z" fill="#ffd84d"/>')
        return "".join(o) + "</svg>"
    o.append('<rect width="800" height="500" fill="url(#a)"/>')
    if "stars" in ex:
        o += ['<circle cx="%d" cy="%d" r="%.1f" fill="#fff" opacity=".8"/>' % (r.randint(0, 800), r.randint(0, 240), r.random() * 1.8 + .6) for _ in range(70)]
    o.append('<circle cx="580" cy="285" r="62" fill="%s" opacity=".92"/><rect y="300" width="800" height="200" fill="url(#b)"/>'
             '<rect x="545" y="305" width="70" height="170" fill="%s" opacity=".18"/>' % (sun, sun))
    o += ['<path d="M0 %d q50 -14 100 0 t100 0 t100 0 t100 0 t100 0 t100 0 t100 0 t100 0" fill="none" stroke="#fff" stroke-opacity=".%d" stroke-width="2"/>' % (320 + i * 26, 10 + i * 3) for i in range(7)]
    if "island" in ex:
        o.append('<path d="M500 302Q610 215 780 302Z" fill="#17594a"/><path d="M560 302Q660 250 800 302Z" fill="#1f7a52"/>')
    if "town" in ex:
        o.append('<path d="M420 302Q560 200 800 240V302Z" fill="#c9a77c"/>')
        for i in range(14):
            h = r.randint(26, 62)
            x = 440 + i * 25
            o.append('<rect x="%d" y="%d" width="21" height="%d" fill="%s"/><path d="M%d %d l12 -10 l12 10z" fill="#d1603d"/>' % (x, 302 - h, h, r.choice(["#fff", "#ffe9b0", "#fbd0c0"]), x - 2, 302 - h))
    if "ship" in ex:
        o.append('<g transform="translate(300 205)"><path d="M0 70H330L300 108H35Z" fill="#fff"/><path d="M8 80H322L317 92H14Z" fill="#d64545"/>'
                 '<rect x="40" y="40" width="250" height="30" fill="#f4f7fa"/><rect x="80" y="14" width="170" height="28" fill="#e4ebf0"/>'
                 '<rect x="120" y="-6" width="90" height="22" fill="#f4f7fa"/><rect x="160" y="-34" width="26" height="30" fill="#0f8fa3"/>'
                 + "".join('<circle cx="%d" cy="55" r="3" fill="#0a2a43"/>' % (52 + i * 12) for i in range(20))
                 + '<path d="M20 112q80 10 190 0t120 0" stroke="#fff" opacity=".5" fill="none"/></g>')
    if "palms" in ex:
        o.append('<path d="M0 500V420Q160 360 330 440V500Z" fill="#f1d49a"/>' + palm(70, 270, 1) + palm(210, 340, .6))
    if "window" in ex:
        o.append('<path fill-rule="evenodd" fill="#efe6da" d="M0 0H800V500H0Z M150 60H650V330H150Z"/><rect x="150" y="60" width="500" height="270" fill="none" stroke="#fff" stroke-width="12"/>'
                 '<rect x="100" y="360" width="600" height="140" rx="20" fill="#fff"/><rect x="100" y="425" width="600" height="75" fill="#0f9aa8"/>'
                 '<rect x="140" y="372" width="160" height="50" rx="18" fill="#e3f2f5"/>')
    if "pool" in ex:
        o.append('<rect y="380" width="800" height="120" fill="#cdb998"/><rect x="110" y="400" width="580" height="75" rx="14" fill="#2ec4d6"/>'
                 + "".join('<path d="M%d 400V475" stroke="#fff" opacity=".4"/>' % (x) for x in range(190, 690, 80)))
    return "".join(o) + "</svg>"


def make_images():
    os.makedirs("images", exist_ok=True)
    for k, v in SCENES.items():
        with open("images/%s.svg" % k, "w") as f:
            f.write(scene(*v))


# ---------- layout ----------
MAIN = ["index.html", "search.html", "overview.html", "cabins.html", "themed.html", "help.html"]
HERO = {
    "register.html": ("Create your account", "Verify your ID once and board faster on every cruise.", "pool"),
    "dashboard.html": ("Your trips at a glance", "Bookings, payments and alerts in one place.", "ship"),
    "search.html": ("Find your cruise", "Filter by destination, duration, budget and cruise line.", "caribbean"),
    "itinerary.html": ("Plan every day at sea", "Build a day-by-day schedule of ports, activities and meals.", "goa"),
    "activity.html": ("Things to do onboard and ashore", "Pick the experiences you want in your package.", "pool"),
    "food.html": ("Dine your way", "Tell us what you eat and when, and we will set the table.", "food"),
    "overview.html": ("Meet the ships", "Facilities, cabins, ratings and departure ports.", "ship"),
    "cabins.html": ("Choose your cabin", "From cosy interiors to suites with a private balcony.", "cabin"),
    "help.html": ("We are here to help", "Answers to common questions and a direct line to support.", "lakshadweep"),
    "review.html": ("What travellers say", "Stories from guests who have sailed with us.", "med"),
    "rating.html": ("Rate your voyage", "Your feedback helps other travellers choose well.", "night"),
    "themed.html": ("Holidays built around you", "Honeymoon, family, adventure, wellness and more.", "caribbean"),
    "payment.html": ("Review and pay", "Check your booking summary and choose how to pay.", "ship"),
    "contact.html": ("Talk to us", "Questions about a booking? Write to us any time.", "goa"),
}


def build_nav(cur):
    labels = dict(pages)
    a = lambda f: '<a href="%s"%s>%s</a>' % (f, ' class="on"' if f == cur else "", labels[f])
    more = "".join(a(f) for f in labels if f not in MAIN + ["login.html", "register.html"])
    return ('<header class="top"><div class="wrap bar"><a class="brand" href="index.html">&#128674; Cruise<span>Booking</span></a>'
            '<button class="burger" aria-label="Menu">&#9776;</button><nav class="links">'
            + "".join(a(f) for f in MAIN)
            + '<div class="dd"><button>More &#9662;</button><div class="dd-menu">' + more + '</div></div>'
            '<a class="btn ghost" href="login.html">Login</a><a class="btn" href="register.html">Register</a></nav></div></header>')


FOOTER = """<footer><div class="wrap"><div class="fcols">
<div><h4>Cruise Booking System</h4><p>Search, plan and book cruise holidays from Mumbai, Goa, Kochi and Chennai to the Arabian Sea, the Caribbean and the Mediterranean.</p></div>
<div><h4>Explore</h4><a href="search.html">Search Cruises</a><a href="themed.html">Themed Holidays</a><a href="cabins.html">Cabins</a><a href="food.html">Food Options</a></div>
<div><h4>Support</h4><a href="help.html">Help Center</a><a href="review.html">Reviews</a><a href="payment.html">Payment</a><a href="login.html#agent">Agent Login</a></div>
<div><h4>Contact</h4><p>support@cruisebooking.com</p><p>+91-9876543210</p><p>Marine Drive, Mumbai, India</p></div>
</div><div class="legal">Cruise Booking System | Group 3 Mini Project</div></div></footer>"""

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cruise Booking System - {title}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:wght@500;600&family=Outfit:wght@400;600&display=swap">
<link rel="stylesheet" href="style.css">
</head>
<body>
{nav}
<main>
{main}
</main>
{footer}
<script src="main.js"></script>
</body>
</html>
"""


def wrap(current, title, body):
    h = HERO.get(current)
    main = body
    if h:
        main = ('<section class="hero sm"><img src="%s" alt=""><div class="wrap"><h1>%s</h1><p>%s</p></div></section>'
                '<div class="wrap page">%s</div>' % (IMG[h[2]], h[0], h[1], body))
    return PAGE.format(title=title, nav=build_nav(current), main=main, footer=FOOTER)


def card(k, t, d, extra=""):
    return '<article class="card"><img src="%s" alt="%s"><div><h3>%s</h3><p>%s</p>%s</div></article>' % (IMG[k], t, t, d, extra)


def grid(*c):
    return '<div class="grid">' + "".join(c) + "</div>"


def tags(*t):
    return "".join('<span class="tag">%s</span>' % x for x in t)


content = {}

def dest(k, name, line, season, price):
    return card(k, name, line, tags("Best: " + season) + '<p class="price">From Rs. %s</p><a class="btn" href="overview.html">View cruises</a>' % price)


content["index.html"] = f"""
<section class="hero"><img src="{IMG['hero']}" alt="A cruise ship sailing into the sunset">
<div class="wrap"><h1>Sail somewhere you have only seen on postcards</h1>
<p>Compare cruises, pick your cabin, plan each day and pay in one place. Short Goa getaways to ten-day Mediterranean voyages.</p>
<form class="quick" action="search.html">
<select name="destination"><option>Goa</option><option>Lakshadweep</option><option>Caribbean</option><option>Mediterranean</option></select>
<select name="departure_city"><option>Mumbai</option><option>Kochi</option><option>Chennai</option><option>Goa</option></select>
<select name="duration"><option>2-3 Days</option><option>5 Days</option><option>7 Days</option><option>10+ Days</option></select>
<input type="submit" value="Search cruises"></form></div></section>

<section class="sec"><div class="wrap"><h2>Featured destinations</h2>
<p>Four routes our travellers book most, with the cruise line that sails them best and the months to go.</p>
{grid(
 dest('goa','Goa','Cordelia Cruises sail a relaxed coastal route with beach stops.','October - March','18,000'),
 dest('lakshadweep','Lakshadweep','Cordelia Cruises visit lagoons, coral and quiet islands.','November - February','35,000'),
 dest('caribbean','Caribbean','Disney Cruise Line mixes island hopping with family shows.','April - August','60,000'),
 dest('med','Mediterranean','Disney Cruise Line calls at hill towns and old harbours.','May - September','1,20,000'))}
</div></section>

<section class="sec alt"><div class="wrap"><h2>How booking works</h2>
<div class="steps">
<div><b>Search</b><br>Filter cruises by destination, departure city, duration, price and cruise line.</div>
<div><b>Choose a cabin</b><br>Compare interior, ocean view, balcony and suite options per person.</div>
<div><b>Plan your trip</b><br>Add activities, meals and a day-by-day itinerary before you pay.</div>
<div><b>Verify and board</b><br>Upload your ID proof once, pay securely and carry your e-ticket.</div>
</div></div></section>

<section class="sec"><div class="wrap"><h2>Why choose us</h2>
<div class="grid">
<div class="feat"><i>&#9973;</i><h3>Easy online booking</h3><p>From search to payment in a few clicks, on phone or desktop.</p></div>
<div class="feat"><i>&#127965;</i><h3>Wide range of destinations</h3><p>Domestic coastlines and international seas, with options for every budget.</p></div>
<div class="feat"><i>&#128467;</i><h3>Customizable itinerary</h3><p>Choose your activities and meals for each day, and change them later.</p></div>
<div class="feat"><i>&#127911;</i><h3>24/7 help centre</h3><p>Ask about cancellations, refunds, cabins or documents any time.</p></div>
<div class="feat"><i>&#11088;</i><h3>Verified reviews</h3><p>Ratings come from guests who have actually sailed.</p></div>
<div class="feat"><i>&#129489;</i><h3>Agent partner portal</h3><p>Travel agents get their own login to manage bookings for clients.</p></div>
</div></div></section>

<section class="sec alt"><div class="wrap"><h2>Holidays for every kind of traveller</h2>
{grid(
 card('pool','Honeymoon Special','Candlelight dinners, couple spa and a balcony cabin.',tags('Love at Sea')+'<br><a href="themed.html">See themed holidays</a>'),
 card('caribbean','Family Vacation','Kids club, family suites and game nights for all ages.',tags('Family Fun Cruise')+'<br><a href="themed.html">See themed holidays</a>'),
 card('lakshadweep','Adventure Trip','Snorkelling, water sports and island trekking.',tags('Thrill Seeker')+'<br><a href="themed.html">See themed holidays</a>'))}
</div></section>

<section class="sec"><div class="wrap"><h2>Guests love the voyage</h2>
<div class="grid">
<blockquote>Great experience, loved the food options.<cite>Rahul S.</cite></blockquote>
<blockquote>The itinerary planner made trip planning very easy.<cite>Divya M.</cite></blockquote>
<blockquote>The cabin was comfortable and the staff very helpful.<cite>Arjun K.</cite></blockquote>
<blockquote>The kids enjoyed the play zone a lot. We will book again.<cite>Meera P.</cite></blockquote>
</div>
<div class="cta"><h2>Your next sunrise is at sea</h2><p>Create an account to save cruises, upload your ID once and book in minutes.</p>
<a class="btn" href="register.html">Create an account</a> <a class="btn ghost" style="color:#fff" href="login.html">Login</a></div>
</div></section>
"""

content["login.html"] = f"""
<section class="auth">
<div class="auth-art"><img src="{IMG['night']}" alt=""><div><h2>Welcome aboard</h2><p>Manage bookings, itineraries and payments from one dashboard.</p></div></div>
<div class="auth-box"><h1>Login</h1><p>Choose how you use Cruise Booking.</p>
<div class="tabs"><button type="button" class="on" data-tab="customer">Customer</button><button type="button" data-tab="agent">Travel agent</button></div>
<div class="pane on" id="customer"><form action="dashboard.html">
<div class="f"><label>Email or mobile number</label><input type="text" name="username" required></div>
<div class="f"><label>Password</label><input type="password" name="password" required></div>
<div class="f"><label><input type="checkbox" name="remember">Remember me</label></div>
<input type="submit" value="Login as customer"></form>
<p>New here? <a href="register.html">Create a customer account</a></p></div>
<div class="pane" id="agent"><form action="dashboard.html">
<div class="f"><label>Agent ID</label><input type="text" name="agent_id" required></div>
<div class="f"><label>Agency code</label><input type="text" name="agency_code" required></div>
<div class="f"><label>Password</label><input type="password" name="password" required></div>
<input type="submit" value="Login as agent"></form>
<p>Agent accounts are verified by our partner team. <a href="contact.html">Contact us</a> to apply.</p></div>
<p><a href="help.html">Forgot password?</a></p></div></section>
"""

content["register.html"] = """
<h2>Customer registration</h2>
<div class="note"><b>Why we ask for ID.</b> Cruise lines must match every passenger to a valid photo ID before boarding. Upload it once and we will reuse it for every booking.</div>
<form class="wide" action="login.html">
<fieldset><legend>Personal details</legend><div class="cols">
<div class="f"><label>Full name (as on ID)</label><input type="text" name="fullname" required></div>
<div class="f"><label>Email</label><input type="email" name="email" required></div>
<div class="f"><label>Phone number</label><input type="tel" name="phone" required></div>
<div class="f"><label>Date of birth</label><input type="date" name="dob" required></div></div>
<div class="f"><label>Gender</label><input type="radio" name="gender" value="male">Male <input type="radio" name="gender" value="female">Female <input type="radio" name="gender" value="other">Other</div></fieldset>
<fieldset><legend>Proof of identity</legend><div class="cols">
<div class="f"><label>ID type</label><select name="id_type"><option>Aadhaar Card</option><option>Passport</option><option>Voter ID</option><option>Driving Licence</option><option>PAN Card</option></select></div>
<div class="f"><label>ID number</label><input type="text" name="id_number" required></div>
<div class="f"><label>Upload ID - front</label><input type="file" name="id_front" accept="image/*,.pdf" required></div>
<div class="f"><label>Upload ID - back</label><input type="file" name="id_back" accept="image/*,.pdf"></div>
<div class="f"><label>Passport-size photo</label><input type="file" name="photo" accept="image/*" required></div>
<div class="f"><label>Nationality</label><input type="text" name="nationality" value="Indian"></div></div>
<p>Accepted: JPG, PNG or PDF. Passport is required for international sailings.</p></fieldset>
<fieldset><legend>Address and emergency contact</legend><div class="f"><label>Residential address</label><textarea rows="3" name="address"></textarea></div><div class="cols">
<div class="f"><label>Emergency contact name</label><input type="text" name="em_name"></div>
<div class="f"><label>Emergency contact phone</label><input type="tel" name="em_phone"></div></div></fieldset>
<fieldset><legend>Create password</legend><div class="cols">
<div class="f"><label>Password</label><input type="password" name="password" required></div>
<div class="f"><label>Confirm password</label><input type="password" name="confirm_password" required></div></div>
<div class="f"><label><input type="checkbox" name="terms" required>I agree to the Terms and Conditions</label></div></fieldset>
<input type="submit" value="Register">
</form>
<p>Already have an account? <a href="login.html">Login here</a>. Travel agent? <a href="login.html#agent">Use the agent login</a>.</p>
"""

content["dashboard.html"] = """
<h2>User Dashboard</h2>
<p>Welcome back, User! Here is a quick summary of your account.</p>

<table border="1" cellpadding="5">
    <tr>
        <th>Upcoming Booking</th>
        <th>Departure Date</th>
        <th>Status</th>
    </tr>
    <tr>
        <td>Empress Cruise - Goa</td>
        <td>15th September</td>
        <td>Confirmed</td>
    </tr>
    <tr>
        <td>Disney Wonder - Caribbean</td>
        <td>2nd December</td>
        <td>Pending Payment</td>
    </tr>
</table>

<h3>Quick Links</h3>
<ul>
    <li><a href="search.html">Search Cruises</a></li>
    <li><a href="itinerary.html">My Itinerary</a></li>
    <li><a href="payment.html">My Bookings & Payments</a></li>
    <li>Profile Settings</li>
    <li>Notification Preferences</li>
    <li><a href="help.html">Help Center</a></li>
</ul>
"""

content["search.html"] = """
<h2>Destination Searching / Filtering</h2>
<form>
    <label>Destination:</label>
    <input type="text" name="destination"><br><br>

    <label>Departure City:</label>
    <select name="departure_city">
        <option>Mumbai</option>
        <option>Chennai</option>
        <option>Kochi</option>
        <option>Goa</option>
    </select><br><br>

    <label>Duration:</label>
    <select name="duration">
        <option>2 Days</option>
        <option>3 Days</option>
        <option>5 Days</option>
        <option>7 Days</option>
        <option>10+ Days</option>
    </select><br><br>

    <label>Price Range:</label>
    <select name="price">
        <option>Below 20,000</option>
        <option>20,000 - 50,000</option>
        <option>50,000 - 1,00,000</option>
        <option>Above 1,00,000</option>
    </select><br><br>

    <label>Cruise Line:</label>
    <select name="cruiseline">
        <option>Cordelia Cruises</option>
        <option>Disney Cruise Line</option>
    </select><br><br>

    <label>Sort By:</label>
    <select name="sort">
        <option>Price - Low to High</option>
        <option>Price - High to Low</option>
        <option>Rating</option>
        <option>Duration</option>
    </select><br><br>

    <input type="submit" value="Search">
    <input type="reset" value="Clear Filters">
</form>

<h3>Search Results (Sample)</h3>
<table border="1" cellpadding="5">
    <tr>
        <th>Cruise Name</th>
        <th>Destination</th>
        <th>Duration</th>
        <th>Price</th>
        <th>Rating</th>
        <th>Action</th>
    </tr>
    <tr>
        <td>Empress Cruise</td>
        <td>Goa</td>
        <td>3 Days</td>
        <td>Rs. 18,000</td>
        <td>4.3</td>
        <td><a href="overview.html">View</a></td>
    </tr>
    <tr>
        <td>Disney Wonder</td>
        <td>Caribbean</td>
        <td>7 Days</td>
        <td>Rs. 60,000</td>
        <td>4.7</td>
        <td><a href="overview.html">View</a></td>
    </tr>
    <tr>
        <td>Empress Explorer</td>
        <td>Lakshadweep</td>
        <td>5 Days</td>
        <td>Rs. 35,000</td>
        <td>4.1</td>
        <td><a href="overview.html">View</a></td>
    </tr>
    <tr>
        <td>Disney Magic</td>
        <td>Mediterranean</td>
        <td>10 Days</td>
        <td>Rs. 1,20,000</td>
        <td>4.8</td>
        <td><a href="overview.html">View</a></td>
    </tr>
</table>
"""

content["itinerary.html"] = """
<h2>Itinerary Planner</h2>
<p>Plan your day-by-day schedule for the duration of your cruise.</p>

<table border="1" cellpadding="5">
    <tr>
        <th>Day</th>
        <th>Port / Location</th>
        <th>Planned Activity</th>
        <th>Meal Plan</th>
    </tr>
    <tr>
        <td>Day 1</td>
        <td>Embarkation - Mumbai</td>
        <td>Welcome Party</td>
        <td>Dinner Buffet</td>
    </tr>
    <tr>
        <td>Day 2</td>
        <td>At Sea</td>
        <td>Pool Games</td>
        <td>All Meals Onboard</td>
    </tr>
    <tr>
        <td>Day 3</td>
        <td>Goa</td>
        <td>Beach Excursion</td>
        <td>Lunch Onshore</td>
    </tr>
    <tr>
        <td>Day 4</td>
        <td>At Sea</td>
        <td>Spa & Relaxation</td>
        <td>All Meals Onboard</td>
    </tr>
    <tr>
        <td>Day 5</td>
        <td>Disembarkation - Mumbai</td>
        <td>Farewell Breakfast</td>
        <td>Breakfast Only</td>
    </tr>
</table>
<br>
<form>
    <label>Add Activity to Day:</label>
    <select name="day">
        <option>Day 1</option>
        <option>Day 2</option>
        <option>Day 3</option>
        <option>Day 4</option>
        <option>Day 5</option>
    </select>
    <input type="text" name="activity" placeholder="Activity Name">
    <input type="submit" value="Add to Itinerary">
</form>
"""

content["activity.html"] = """
<h2>Activity Selection</h2>
<p>Select the onboard and onshore activities you would like included in your package.</p>

<h3>Onboard Activities</h3>
<form>
    <input type="checkbox" name="activity1"> Swimming Pool<br>
    <input type="checkbox" name="activity2"> Live Music Show<br>
    <input type="checkbox" name="activity3"> Casino Night<br>
    <input type="checkbox" name="activity4"> Spa & Wellness<br>
    <input type="checkbox" name="activity5"> Kids Play Zone<br>
    <input type="checkbox" name="activity6"> Gym & Fitness Center<br>
    <input type="checkbox" name="activity7"> Movie Theatre<br>
    <input type="checkbox" name="activity8"> Dance Classes<br><br>

    <h3>Onshore Activities</h3>
    <input type="checkbox" name="activity9"> Snorkeling Excursion<br>
    <input type="checkbox" name="activity10"> City Sightseeing Tour<br>
    <input type="checkbox" name="activity11"> Water Sports<br>
    <input type="checkbox" name="activity12"> Local Market Shopping<br><br>

    <input type="submit" value="Confirm Activities">
</form>
"""

content["food.html"] = """
<h2>Food Options</h2>
<form>
    <label>Meal Preference:</label><br>
    <input type="radio" name="meal" value="veg"> Vegetarian<br>
    <input type="radio" name="meal" value="nonveg"> Non-Vegetarian<br>
    <input type="radio" name="meal" value="vegan"> Vegan<br>
    <input type="radio" name="meal" value="jain"> Jain Food<br><br>

    <label>Cuisine Preference:</label>
    <select name="cuisine">
        <option>Indian</option>
        <option>Continental</option>
        <option>Chinese</option>
        <option>Italian</option>
        <option>Mexican</option>
    </select><br><br>

    <label>Dietary Restrictions:</label><br>
    <input type="checkbox" name="allergy1"> Nut Allergy<br>
    <input type="checkbox" name="allergy2"> Gluten Free<br>
    <input type="checkbox" name="allergy3"> Lactose Free<br><br>

    <label>Preferred Dining Time:</label>
    <select name="dining_time">
        <option>Early Sitting (6:00 PM)</option>
        <option>Late Sitting (8:30 PM)</option>
    </select><br><br>

    <input type="submit" value="Save Food Preference">
</form>

<h3>Sample Menu</h3>
<table border="1" cellpadding="5">
    <tr>
        <th>Meal</th>
        <th>Item</th>
        <th>Type</th>
    </tr>
    <tr>
        <td>Breakfast</td>
        <td>Idli & Sambar</td>
        <td>Vegetarian</td>
    </tr>
    <tr>
        <td>Lunch</td>
        <td>Grilled Chicken</td>
        <td>Non-Vegetarian</td>
    </tr>
    <tr>
        <td>Dinner</td>
        <td>Pasta Alfredo</td>
        <td>Vegetarian</td>
    </tr>
</table>
"""

content["overview.html"] = """
<h2>Individual Cruise Overview</h2>

<h3>Empress Cruise</h3>
<p>Destination: Goa | Duration: 3 Days | Price: Rs. 18,000</p>
<p>Description: A short and relaxing cruise experience along the western coastline,
offering pool activities, live entertainment and a variety of dining options.</p>
<ul>
    <li>Cabin Types: Interior, Ocean View, Balcony, Suite</li>
    <li>Onboard Facilities: Pool, Gym, Spa, Casino</li>
    <li>Rating: 4.3 / 5</li>
    <li>Departure Port: Mumbai</li>
    <li>Ship Capacity: 1800 Passengers</li>
</ul>
<p><a href="cabins.html">Select Cabin</a> | <a href="login.html">Book Now</a></p>

<h3>Disney Wonder</h3>
<p>Destination: Caribbean | Duration: 7 Days | Price: Rs. 60,000</p>
<p>Description: A family-friendly cruise across the Caribbean islands with
themed entertainment, character meet-and-greets and multiple onshore excursions.</p>
<ul>
    <li>Cabin Types: Inside, Outside, Verandah, Concierge Suite</li>
    <li>Onboard Facilities: Water Slides, Theatre, Kids Club, Adult-Only Deck</li>
    <li>Rating: 4.7 / 5</li>
    <li>Departure Port: Miami</li>
    <li>Ship Capacity: 2700 Passengers</li>
</ul>
<p><a href="cabins.html">Select Cabin</a> | <a href="login.html">Book Now</a></p>
"""

content["cabins.html"] = """
<h2>Cabin Selection</h2>
<table border="1" cellpadding="5">
    <tr>
        <th>Cabin Type</th>
        <th>Description</th>
        <th>Price (per person)</th>
        <th>Select</th>
    </tr>
    <tr>
        <td>Interior</td>
        <td>Compact cabin with no window, budget friendly</td>
        <td>Rs. 15,000</td>
        <td><input type="radio" name="cabin"></td>
    </tr>
    <tr>
        <td>Ocean View</td>
        <td>Cabin with a window overlooking the sea</td>
        <td>Rs. 22,000</td>
        <td><input type="radio" name="cabin"></td>
    </tr>
    <tr>
        <td>Balcony</td>
        <td>Private balcony with outdoor seating</td>
        <td>Rs. 30,000</td>
        <td><input type="radio" name="cabin"></td>
    </tr>
    <tr>
        <td>Suite</td>
        <td>Spacious cabin with premium amenities</td>
        <td>Rs. 45,000</td>
        <td><input type="radio" name="cabin"></td>
    </tr>
</table>
<br>
<form>
    <label>Number of Guests:</label>
    <select name="guests">
        <option>1</option>
        <option>2</option>
        <option>3</option>
        <option>4</option>
    </select><br><br>
    <input type="submit" value="Confirm Cabin">
</form>
"""

content["help.html"] = """
<h2>Help Center</h2>
<h3>Frequently Asked Questions</h3>
<ol>
    <li>How do I cancel my booking?</li>
    <li>What is the refund policy?</li>
    <li>Can I change my cabin after booking?</li>
    <li>Is travel insurance included in the package?</li>
    <li>What documents are required for boarding?</li>
    <li>Can I customize my itinerary after booking?</li>
</ol>

<h3>Contact Support</h3>
<form>
    <label>Subject:</label><br>
    <input type="text" name="subject"><br><br>

    <label>Your Query:</label><br>
    <textarea rows="4" cols="40"></textarea><br><br>

    <label>Attach Screenshot (if any):</label><br>
    <input type="file" name="attachment"><br><br>

    <input type="submit" value="Submit Query">
</form>
"""

content["review.html"] = """
<h2>Review Page</h2>
<form>
    <label>Cruise Name:</label>
    <input type="text" name="cruisename"><br><br>

    <label>Your Name:</label>
    <input type="text" name="reviewer_name"><br><br>

    <label>Your Review:</label><br>
    <textarea rows="4" cols="40"></textarea><br><br>

    <input type="submit" value="Submit Review">
</form>

<h3>Existing Reviews</h3>
<p><b>Rahul S.</b> - "Great experience, loved the food options."</p>
<p><b>Divya M.</b> - "Itinerary planner made trip planning very easy."</p>
<p><b>Arjun K.</b> - "Cabin was comfortable and the staff was very helpful."</p>
<p><b>Meera P.</b> - "Kids enjoyed the play zone a lot, will book again."</p>
"""

content["rating.html"] = """
<h2>Cruise Rating Page</h2>
<form>
    <label>Rate this Cruise:</label><br>
    <input type="radio" name="rating" value="1"> 1
    <input type="radio" name="rating" value="2"> 2
    <input type="radio" name="rating" value="3"> 3
    <input type="radio" name="rating" value="4"> 4
    <input type="radio" name="rating" value="5"> 5
    <br><br>

    <label>Rate Onboard Food:</label><br>
    <input type="radio" name="food_rating" value="1"> 1
    <input type="radio" name="food_rating" value="2"> 2
    <input type="radio" name="food_rating" value="3"> 3
    <input type="radio" name="food_rating" value="4"> 4
    <input type="radio" name="food_rating" value="5"> 5
    <br><br>

    <label>Rate Staff Service:</label><br>
    <input type="radio" name="staff_rating" value="1"> 1
    <input type="radio" name="staff_rating" value="2"> 2
    <input type="radio" name="staff_rating" value="3"> 3
    <input type="radio" name="staff_rating" value="4"> 4
    <input type="radio" name="staff_rating" value="5"> 5
    <br><br>

    <input type="submit" value="Submit Rating">
</form>

<h3>Average Ratings</h3>
<table border="1" cellpadding="5">
    <tr>
        <th>Category</th>
        <th>Average Rating</th>
    </tr>
    <tr>
        <td>Overall Experience</td>
        <td>4.5 / 5</td>
    </tr>
    <tr>
        <td>Food Quality</td>
        <td>4.3 / 5</td>
    </tr>
    <tr>
        <td>Staff Service</td>
        <td>4.7 / 5</td>
    </tr>
</table>
"""

content["themed.html"] = """
<h2>Themed Holiday Planner</h2>
<form>
    <label>Choose a Theme:</label><br>
    <input type="radio" name="theme" value="honeymoon"> Honeymoon Special<br>
    <input type="radio" name="theme" value="family"> Family Vacation<br>
    <input type="radio" name="theme" value="adventure"> Adventure Trip<br>
    <input type="radio" name="theme" value="wellness"> Wellness Retreat<br>
    <input type="radio" name="theme" value="solo"> Solo Traveller<br>
    <input type="radio" name="theme" value="senior"> Senior Citizen Special<br><br>

    <label>Preferred Month:</label>
    <select name="month">
        <option>January</option>
        <option>April</option>
        <option>July</option>
        <option>October</option>
        <option>December</option>
    </select><br><br>

    <input type="submit" value="Plan My Holiday">
</form>

<h3>Popular Themed Packages</h3>
<table border="1" cellpadding="5">
    <tr>
        <th>Package Name</th>
        <th>Theme</th>
        <th>Includes</th>
    </tr>
    <tr>
        <td>Love at Sea</td>
        <td>Honeymoon Special</td>
        <td>Candlelight Dinner, Couple Spa, Balcony Cabin</td>
    </tr>
    <tr>
        <td>Family Fun Cruise</td>
        <td>Family Vacation</td>
        <td>Kids Club, Family Suite, Game Nights</td>
    </tr>
    <tr>
        <td>Thrill Seeker</td>
        <td>Adventure Trip</td>
        <td>Snorkeling, Water Sports, Island Trekking</td>
    </tr>
</table>
"""

content["payment.html"] = """
<h2>Payment / Booking Summary</h2>
<table border="1" cellpadding="5">
    <tr>
        <th>Item</th>
        <th>Details</th>
        <th>Amount</th>
    </tr>
    <tr>
        <td>Cruise Package</td>
        <td>Empress Cruise - Goa (3 Days)</td>
        <td>Rs. 18,000</td>
    </tr>
    <tr>
        <td>Cabin Upgrade</td>
        <td>Balcony Cabin</td>
        <td>Rs. 12,000</td>
    </tr>
    <tr>
        <td>Activities</td>
        <td>Snorkeling, Spa</td>
        <td>Rs. 3,000</td>
    </tr>
    <tr>
        <td><b>Total</b></td>
        <td></td>
        <td><b>Rs. 33,000</b></td>
    </tr>
</table>
<br>
<form>
    <label>Payment Method:</label><br>
    <input type="radio" name="payment"> Credit / Debit Card<br>
    <input type="radio" name="payment"> Net Banking<br>
    <input type="radio" name="payment"> UPI<br>
    <input type="radio" name="payment"> Wallet<br><br>

    <input type="submit" value="Proceed to Pay">
</form>
"""

content["contact.html"] = """
<h2>Contact Us</h2>
<p>Email: support@cruisebooking.com</p>
<p>Phone: +91-9876543210</p>
<p>Address: Cruise Booking Pvt Ltd, Marine Drive, Mumbai, India</p>

<form>
    <label>Name:</label>
    <input type="text" name="contact_name"><br><br>

    <label>Email:</label>
    <input type="email" name="contact_email"><br><br>

    <label>Message:</label><br>
    <textarea rows="4" cols="40"></textarea><br><br>

    <input type="submit" value="Send Message">
</form>
"""


def feat(i, t, d):
    return '<div class="feat"><i>%s</i><h3>%s</h3><p>%s</p></div>' % (i, t, d)


def faq(q, a):
    return "<details><summary>%s</summary><p>%s</p></details>" % (q, a)


extras = {
    "dashboard.html": grid(
        '<div class="stat"><b>2</b>Upcoming trips</div>', '<div class="stat"><b>1</b>Payment pending</div>',
        '<div class="stat"><b>1,250</b>Loyalty points</div>', '<div class="stat"><b>Verified</b>ID proof status</div>'),
    "overview.html": "<h3>Onboard gallery</h3>" + grid(
        card("ship", "The ship", "Multi-deck liners with open promenades, theatres and dining rooms."),
        card("pool", "Pool deck", "Sun loungers, water slides and a bar by the water."),
        card("night", "Evenings at sea", "Live music, dance floors and casino nights under the stars.")),
    "cabins.html": "<h3>In every cabin</h3>" + grid(
        feat("&#128716;", "Comfortable beds", "Twin or double, with fresh linen daily."),
        feat("&#128703;", "Private bathroom", "Shower, toiletries and towels provided."),
        feat("&#128250;", "Entertainment", "TV with ship channels and movies."),
        feat("&#129489;", "Cabin steward", "Housekeeping twice a day, and room service.")),
    "food.html": "<h3>Where you will eat</h3>" + grid(
        card("food", "Live kitchens", "Chefs cook Indian, Continental, Chinese, Italian and Mexican dishes in front of you."),
        card("pool", "Sunset deck dining", "Grills and light bites served by the pool as the sun goes down."),
        card("night", "Late-night bites", "Snacks, coffee and desserts after the show.")),
    "activity.html": "<h3>Popular experiences</h3>" + grid(
        card("pool", "Pool and spa", "Swim, unwind and book a couple or solo spa session."),
        card("night", "Shows and casino", "Live music every evening and casino night once per voyage."),
        card("goa", "Shore excursions", "Beach days, city tours, snorkelling and local markets.")),
    "themed.html": "<h3>Themes at a glance</h3>" + grid(
        card("pool", "Honeymoon Special", "Private dinners, couple spa and a balcony cabin.", tags("Candlelight Dinner", "Couple Spa")),
        card("caribbean", "Family Vacation", "Kids club, family suites and evening games.", tags("Kids Club", "Game Nights")),
        card("lakshadweep", "Adventure Trip", "Snorkelling, water sports and island trekking.", tags("Snorkeling", "Trekking"))),
    "help.html": "<h3>Answers</h3>" + "".join([
        faq("How do I cancel my booking?", "Open your dashboard, choose the booking and select Cancel. Refund amounts depend on how close you are to departure."),
        faq("What is the refund policy?", "Refunds are returned to your original payment method. Earlier cancellations receive a larger refund."),
        faq("Can I change my cabin after booking?", "Yes, subject to availability. Price differences are shown before you confirm."),
        faq("Is travel insurance included?", "It is optional. You can add it from the payment summary."),
        faq("What documents are required for boarding?", "A valid photo ID that matches your booking, uploaded at registration. International sailings need a passport."),
        faq("Can I customize my itinerary after booking?", "Yes. Use the Itinerary Planner to add or remove activities and meals.")]),
    "contact.html": "<h3>Office hours</h3><p>Monday to Saturday, 9:00 AM to 7:00 PM IST. Help Center answers are available 24/7.</p>",
}

make_images()
for filename, title in pages:
    html = wrap(filename, title, content[filename] + extras.get(filename, ""))
    with open(filename, "w") as f:
        f.write(html)

print("Generated", len(pages), "pages and", len(SCENES), "images.")
