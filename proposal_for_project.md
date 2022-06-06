# Capstone Proposal

### General Design
1. This application will be designed to store BBGrand Piano Studio clients with the owner having the ability to have full CRUD functionality from BBGrand owner login. The ability to email single clients, and email all clients as well using clients email application

2. The BBGrand piano student would be able to do CRU functions, only viewing the children associated with the correct guardian record for that client.

### Database Model Design
- The database for each record will include a first name, last name, phone number, email and home address for the guardian. These will all be required fields. There will also be an associated table to the guardian where they will enter their students first name and last name. That is all that will be required for this table and these will all be required fields also. The guardian would also have the ability to email through their view as well.

### Planned APIS For Project At This Time
- Incorporate an API called **Nylas** that would handle emailing right from the application on the client view through a link on the displayed client information. If there becomes a cost to this API, **google&#39;s email API** will be the next choice. I would also like to incorporate the **Mapquest API** for *geocaching*. This is so the BBGrand owner on her view can get directions to someone&#39;s house for dropping off materials to the student if needed.

### Use of CMA in BBGrand Studio
- After meeting with the owner of BBGrand piano studio and deciding to sign up for lessons. The parent can create a login for the app. They will then register themselves as the guardian. Next they will be redirected to a page to enter a student first name and last name. They will be able to continue to do this with redirects back to this page for as many students as they are enrolling into BBGrand piano studio.

### Possible Future Features
- As the application grows possible improvements could include, automating billing with invoices sent to guardians and payments with stripe API into this application.
