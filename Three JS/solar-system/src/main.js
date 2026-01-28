import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

// creating scene
const scene = new THREE.Scene();

// creating camere
const camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);
camera.position.z = 60;

// creating renderer
const canvas = document.querySelector("canvas.canvas");
const renderer = new THREE.WebGLRenderer({
  canvas: canvas,
});
renderer.setSize(window.innerWidth, window.innerHeight);

const orbit = new OrbitControls(camera, canvas);

// Adding Meshes
const sphereGeometry = new THREE.SphereGeometry(1, 32, 32);

const sunMaterial = new THREE.MeshBasicMaterial({ color: 0xfff700 });
const sun = new THREE.Mesh(sphereGeometry, sunMaterial);
sun.scale.setScalar(5);
scene.add(sun);

const earthMaterial = new THREE.MeshBasicMaterial({ color: "blue" });
const earth = new THREE.Mesh(sphereGeometry, earthMaterial);
earth.position.x = 10;
scene.add(earth);

const moonMaterial = new THREE.MeshBasicMaterial({ color: "grey" });
const moon = new THREE.Mesh(sphereGeometry, moonMaterial);
moon.position.x = 2;
moon.scale.setScalar(0.3);
earth.add(moon);

function renderLoop() {
  renderer.render(scene, camera);
  requestAnimationFrame(renderLoop);
}

renderLoop();
