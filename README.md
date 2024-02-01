

**Welcome to rest_ajax_102: Your API Fetching Playground!**

Greetings from the exciting world of API fetching in Django REST Framework! Brace yourselves for an adventure in crafting dynamic frontend experiences. ✨

**Mission Briefing:**

Your task is to fetch product data from our custom API and display it beautifully on the frontend, showcasing your JavaScript and frontend development skills.

**Basecamp Setup:**

1. **Clone the Repository:**

   Begin by teleporting the project to your local machine: `git clone <repository_url>`

2. **Install Dependencies:**

   Activate your virtual environment and install the required packages:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Deploy Data:**

   Populate the database with essential information:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py loaddata data.json
   ```

   - Encountering issues with `loaddata`? Feel free to insert data manually.

**Mission Objectives:**

1. **Fetch and Display the Product List:**

   - Employ your JavaScript expertise, specifically jQuery, to retrieve product data from our API.
   - Construct a visually appealing product display within a dedicated page.
   - Ensure url navigation by linking this page from `index.html` and creating a corresponding URL pattern for its template for ease of access.



**2. Build Your Own API:**

- Go to the "shop" app's API section and add code for the "Order" model. Think of it as a special message sender for Order info.
- Use a "Serializer" to define exactly what data gets sent through that message. It's like a packing list for the message!
- Send a test message using your new code and display the data on your website. High five for success!

**3. Order Details: More Puzzles to Solve:**

- Remember how Orders and Addresses are connected? We'll do the same, but for both!
- Make sure your "Serializer" understands this connection and packs the data correctly. It's like a combined packing list for Order and Address!
- Conquered this? You're a coding warrior! Now level up your app:
    - Make it look prettier and easier to use.
    - Add more ways to handle data (like lists and filters).
    - Improve the structure of your data (imagine better boxes for packing!).

**Onward to API mastery!** 

