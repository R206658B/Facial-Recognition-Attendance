## Overview of the Application

1. ### Home page 

    First, with our face recognition app, members can simply stand in front of a camera and their faces will be scanned and matched against a pre-existing image of registered members. Once the system identifies the member, the attendance will be marked as present automatically. This app can also be integrated with the member AD databases so that supervisor can easily keep track of attendance in real-time. 

    Not only does this app save time and reduce the administrative burden on instructors, but it also enhances security and reduces the risk of impersonation or cheating. Additionally, the face recognition app can generate detailed reports and analytics on member attendance, providing valuable insights to educators and administrators to make informed decisions. 

    Overall, the face recognition app is a game-changing technology that can streamline attendance taking and improve the overall efficiency and effectiveness of educational institutions. 
    
2. ### Add New Student Page 

    - The member navigates to the "Add New Student" page on the app. 

    - The member takes a picture of themselves using the camera within the app. 

    - The page displays a preview of the image, and prompts the member to confirm whether or not they want to use this image as their profile picture. 

    - the page prompts them to enter their name. 

    - The member enters their name into a text field. 

    - The app saves the image and the member's name to a server for use in the attendance phase later.

    The app uses OpenCV library to allow the student to take a picture. 

    The app uses facial-recognition library to detect and identify the face in the image. 

    The app saves the image file to a designated directory storage location. 

    The app prompts the student to enter their name using a text field. 

    When the member enters their name, the app saves it. 

    The app stores the image file and the associated name in a way that will allow it to be used for attendance tracking later. 
    
3. ### Attendance with camera Page 

    - The member navigates to the "Attendance With Camera" page  

    - It displays two choices: "Create New Attendance Sheet" or "View Sheets". 

    - If the member chooses to create a new attendance sheet, The student enters a name for the sheet in a text field. 

    - The app creates a new attendance sheet with the name provided by the member. 

    - If the member chooses to view created sheets, the app displays a list of previously created attendance sheets. 

    - The member selects a previously created sheet from the list using a drop-down or similar interface. and the app automatically renames the selected sheet with the current date appended to the name. 

    - The app displays two buttons: "Start Taking Attendance" and "Cancel". 

    - The code uses face recognition to scan the camera feed for faces. 

    If a member is recognized as being in the database, a rectangle box is drawn around their face with their name written above the box. 

    If a member is not recognized, a rectangle box is drawn around their face with the word "Unknown" written above the box. 

    - The code adds the member's attendance status (present/absent) to the current attendance sheet. 

    - Program continues scanning for faces and adding attendance statuses until the student clicks the "Stop Taking Attendance" button. 

    - When the member clicks the "Stop Taking Attendance" button, the app saves the current attendance sheet to a or server.

4. ### Manual Attendance Page 

    - The member navigates to the "Manual Attendance" page  

    - There are two options: Create new attendance sheet or view created sheet. 

    - You can then Add record manually in the selected sheet 


