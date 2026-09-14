# GUI Viewer Controls Task

## Before you begin

This task uses **Node.js** and **npm**. Install a current Node.js LTS release if they are not already available on your machine.

From the `GUI-Task` folder, install the project dependencies and start the development server:

```bash
npm install
npm start
```

The app opens in a browser at the URL printed by the development server, normally `http://localhost:3000`.

## Front-end tools used here

### React

React is our primary framework for front-end web development. It follows a component-based architecture, where the user interface is divided into reusable, self-contained components. Each component manages its own logic, state, and rendering behaviour. This modular approach enables developers to build complex user interfaces by combining smaller, manageable components.

If you need a refresher, use Programming with Mosh's [React tutorial for beginners](https://www.youtube.com/watch?v=SqcY0GlETPk).

### JavaScript, HTML, and CSS

Use JavaScript for behaviour and state, HTML for page structure, and CSS for presentation. The project already includes Tailwind CSS; using Tailwind is optional for this task. Plain CSS is acceptable.

### Node.js and npm

Node.js runs the development tooling and npm installs the project's packages and runs its scripts. You do not need to install React, Three.js, or Tailwind globally.

## Provided starting point

You start with a React app containing a Three.js viewer with a 3D model of a robot. The viewer is already implemented in `src/URDFViewer.jsx`.

You do **not** need prior experience with Three.js, 3D programming, or URDF files. The viewer exposes 5 functions, which is what you will use, instead of interacting with the Three.js world directly:

```js
window.roverViewer.setBrightness(value)
window.roverViewer.setZoom(value)
window.roverViewer.setPanX(value)
window.roverViewer.setPanY(value)
window.roverViewer.setPanZ(value)
```

The values are clamped by the viewer:

| Function | Input range |
| --- | --- |
| `setBrightness(value)` | `0` to `2` |
| `setZoom(value)` | `0` to `1` |
| `setPanX(value)` | `-2` to `2` |
| `setPanY(value)` | `-2` to `2` |
| `setPanZ(value)` | `-2` to `2` |

## Your task

Build controls for the rover viewer.

Your UI must include:

1. A way to control the brightness of the Three.js viewer.
2. A way to zoom the camera in and out of the Three.js viewer.
3. A way to select hardcoded profiles that immediately set both Brightness and Zoom. Define at least two profiles, with values inside the API ranges.
4. Data persistence with `localStorage`. The most recent brightness and zoom values must be restored and applied when the app is opened in a later browser session. Selecting a profile should also update the saved values.

Keep the controls easy to understand. In particular, use visible labels and make the selected profile clear.

Do NOT edit `URDFViewer.jsx`.

## Verify your work

1. Run `npm start` and open the app.
2. Adjust the Brightness and Zoom controls. Confirm each one works as intended.
3. Select each profile and confirm it updates both controls and the viewer.
4. Change the values, refresh the browser, and confirm the latest values are restored.
