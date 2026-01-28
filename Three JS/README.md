# Three.js Practice Projects

A collection of practice projects exploring Three.js 3D graphics library with various concepts and techniques.

## 🎯 Projects Overview

### 1. **hello-world**

Starting point for learning Three.js basics.

- Basic scene setup
- Camera and renderer configuration
- Creating and rendering 3D objects
- **Tech Stack:** Three.js, Vite, JavaScript

### 2. **orbit-control**

Implementation of interactive 3D scene navigation.

- Orbit controls for camera manipulation
- Mouse interaction handling
- 3D object rendering and rotation
- **Tech Stack:** Three.js, OrbitControls addon, Vite

### 3. **orthographic-camera**

Exploring different camera projection modes.

- Orthographic camera setup
- Comparison with perspective camera
- Flat 2D-like rendering in 3D space
- **Tech Stack:** Three.js, OrbitControls addon, Vite

### 4. **solar-system**

A more complex project demonstrating orbital mechanics.

- Multiple objects in 3D space
- Orbital motion simulation
- Scene organization and hierarchy
- Camera positioning and controls
- **Tech Stack:** Three.js, OrbitControls addon, Vite

## 🚀 Getting Started

### Prerequisites

- Node.js (v16 or higher recommended)
- npm or yarn package manager

### Installation

Each project can be set up independently:

```bash
cd [project-name]
npm install
```

### Running a Project

Development mode with hot reload:

```bash
npm run dev
```

Build for production:

```bash
npm run build
```

Preview production build:

```bash
npm run preview
```

## 📁 Project Structure

Each project follows this structure:

```
[project-name]/
├── src/
│   ├── main.js       # Main Three.js application
│   ├── style.css     # Styling
├── public/           # Static assets
├── index.html        # HTML entry point
├── package.json      # Project dependencies
└── vite.config.js    # Vite configuration (if present)
```

## 🛠️ Technologies Used

- **Three.js** - JavaScript 3D graphics library
- **Vite** - Fast build tool and development server
- **JavaScript (ES6+)** - Modern JavaScript
- **WebGL** - 3D graphics rendering

## 📚 Key Concepts Covered

- Scene management
- Cameras (Perspective & Orthographic)
- Geometry and Materials
- Mesh creation and manipulation
- Lighting and Shading
- Camera controls (OrbitControls)
- Animation loops
- User interaction

## 🎨 Features

- Interactive 3D visualization
- Real-time rendering
- Responsive canvas sizing
- Mouse controls for camera manipulation
- Modular project structure
- Modern development workflow with Vite

## 📖 Learning Resources

- [Three.js Official Documentation](https://threejs.org/docs/)
- [Three.js Examples](https://threejs.org/examples/)
- [WebGL Fundamentals](https://webglfundamentals.org/)

## 📝 Notes

- Each project is self-contained and can be run independently
- Experiments and commented code are preserved for learning purposes
- Projects build upon each other with increasing complexity

## 📄 License

This project is open source and available under the MIT License.

---

**Created as a practice repository for learning Three.js concepts and 3D graphics programming.**
