# Learning Management System (LMS)

## **Overview**
The Learning Management System (LMS) is a web application inspired by the functionality of Google Classroom. It provides a platform where teachers can create and manage classes, and students can join these classes seamlessly. Teachers can upload content, track student progress, and analyze how much time each student spends on specific materials, enabling a more personalized and effective learning experience.

---

## **Why I Made It**
I created this LMS to address the need for a structured, efficient, and insightful platform for online learning. While platforms like Google Classroom provide excellent tools for class and content management, I wanted to include a key feature: **tracking how much time students spend on specific content**. This feature allows teachers to monitor engagement and adapt their teaching strategies based on real-time data.

Through this project, I aimed to:
- Deepen my understanding of backend and frontend web development.
- Learn how to implement features like user authentication, content management, and data analytics.
- Build a real-world project showcasing problem-solving and technical skills.

---

## **Key Features**
- **Class Management**:
  - Teachers can create classes with unique passkeys.
  - Students can join classes using the passkey shared by the teacher.

- **Content Upload**:
  - Teachers can upload learning materials (e.g., PDFs, videos, assignments) for students to access.

- **Progress Tracking**:
  - Tracks the time each student spends on specific content.
  - Provides detailed reports for teachers to monitor student engagement.

- **Role-Based Authentication**:
  - Teachers and students have separate dashboards.
  - Secure login system to ensure data privacy and accessibility.

---

## **Technologies Used**
- **Backend**: Django framework for creating models, views, and handling authentication.
- **Frontend**: Tailwind CSS for crafting a responsive and visually appealing interface.
- **Data Visualization**: Matplotlib (Python) for generating progress reports and visual charts.
- **Database**: SQLite (Django default) for data storage and management.

---

## **What I Learned**
While building this project, I gained valuable skills and knowledge, including:
1. **Backend Development**:
   - Creating models for role-based users (teachers and students).
   - Implementing secure login and session management.
2. **Frontend Development**:
   - Designing a responsive UI with Tailwind CSS.
   - Ensuring a seamless user experience for teachers and students.
3. **Data Analytics**:
   - Tracking time spent by users on content and visualizing it with Matplotlib.
   - Storing and processing data efficiently.
4. **Full-Stack Integration**:
   - Combining Django with Tailwind CSS to build a complete web application.
5. **Problem-Solving**:
   - Debugging issues with class creation, authentication, and time tracking.

---

## **How It Works**
1. **Teachers**:
   - Sign up and log in as a teacher.
   - Create a class with a course name, description, and unique passkey.
   - Upload learning materials for students to access.
   - View detailed reports on student engagement and time tracking.

2. **Students**:
   - Sign up and log in as a student.
   - Join a class using the passkey provided by the teacher.
   - Access learning materials and engage with the course content.

---

## **Future Improvements**
- Integrate live quizzes and grading features.
- Add notifications for assignment deadlines and new content uploads.
- Enable support for multiple file types (e.g., images, audio).
- Implement a leaderboard to gamify learning and increase engagement.

---

## **Getting Started**
To set up and run the project locally:
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install dependencies:
   ```bash
   pip install django
   make migration
   ```
3. Run the development server:
   ```bash
   python manage.py runserver
   ```
## 🤝 Contributing

### Clone the repo

```bash
git clone the repo
cd lms
```

### Build the project

```bash
pip install reqiment.txt
```

### Run the project

```bash
python django 
```


```
### Submit a pull request

If you'd like to contribute, please fork the repository and open a pull request to the `main` branch.
