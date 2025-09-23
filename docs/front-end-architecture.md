# Front-End Architecture: Monkey Logs

## 1. Technology Stack

### Mobile App (Individual & Student)

- **Primary Framework:** React Native. This allows for a single codebase for both iOS and Android.
- **State Management:** Redux Toolkit or Zustand. For a project of this scale, a predictable state container is essential. Redux Toolkit provides a standard, robust solution, while Zustand is a more lightweight and modern alternative.
- **Styling:** A library like Styled Components or NativeBase for a consistent and component-based styling approach.
- **Networking:** Axios for making API calls to the Python backend.

### Web Portal (Coach)

- **Primary Framework:** React with TypeScript.
- **State Management:** Redux Toolkit or Zustand. Maintaining consistency with the mobile app's state management library is a good practice for teams and shared knowledge.
- **Styling:** Styled Components or a utility-first CSS framework like Tailwind CSS.
- **UI Component Library:** A professional library like Material-UI or Ant Design to accelerate the development of the data-heavy dashboards and tables.
- **Data Visualization:** A charting library like Chart.js or Recharts to display analytics on student performance.
- **Networking:** Axios for API calls.

## 2. Frontend System Architecture

The frontends will operate as two separate applications, each handling its own state and UI logic, but sharing a common set of API endpoints from the backend.

### Mobile App Architecture

The app will be structured with a clear separation of concerns:

- **screens/:** Contains the main views for authentication, logging, dashboard, and training plans.
- **components/:** Reusable UI elements like buttons, input fields, and custom log cards.
- **store/:** Handles state management (e.g., Redux store, actions, reducers).
- **api/:** Manages all communication with the backend API.
- **Navigation:** React Navigation will be used to manage the app's flow and screen transitions.

### Web Portal Architecture

The web app will be structured to handle the complex, data-intensive views for coaches:

- **pages/:** Contains the main pages for the team dashboard, student profiles, and workout builder.
- **components/:** Reusable components, particularly for data tables and charts.
- **store/:** Manages the application state.
- **api/:** Manages all communication with the backend.
- **Routing:** React Router will be used to manage the portal's URL-based navigation.
