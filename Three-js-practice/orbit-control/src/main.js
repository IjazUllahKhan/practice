import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  500
);
camera.position.z = 5;
const canvas = document.querySelector("canvas.canvas");
const renderer = new THREE.WebGLRenderer({ canvas: canvas });

renderer.setSize(window.innerWidth, window.innerHeight);

const geometry = new THREE.BoxGeometry(1, 1, 1);
const material = new THREE.MeshBasicMaterial({ color: 0xff0000 });
const cube = new THREE.Mesh(geometry, material);

scene.add(cube);

const orbit = new OrbitControls(camera, canvas);

orbit.enableDamping = true;
orbit.autoRotate = true;

function renderLoop() {
  window.requestAnimationFrame(renderLoop);
  orbit.update();
  renderer.render(scene, camera);
}

renderLoop();
