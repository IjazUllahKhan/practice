// import * as THREE from "three";

// const scene = new THREE.Scene();
// const camera = new THREE.PerspectiveCamera(
//   75,
//   window.innerWidth / window.innerHeight,
//   0.1,
//   1000
// );

// const renderer = new THREE.WebGLRenderer();
// renderer.setSize(window.innerWidth, window.innerHeight);
// renderer.setAnimationLoop(animate);
// document.body.appendChild(renderer.domElement);

// const geometry = new THREE.BoxGeometry(1, 1, 1);
// const material = new THREE.MeshBasicMaterial({ color: 0xff0000 });
// const cube = new THREE.Mesh(geometry, material);
// scene.add(cube);

// const geometry2 = new THREE.BoxGeometry(1, 1, 1);
// const material2 = new THREE.MeshBasicMaterial({ color: 0x0000ff });
// const cube2 = new THREE.Mesh(geometry2, material2);
// scene.add(cube2);

// camera.position.z = 5;
// function animate() {
//   cube.rotation.x += 0.01;
//   cube.rotation.y += 0.01;
//   cube2.position.x = 2;
//   cube2.position.y = -2;
//   cube2.position.z = -2;
//   cube2.rotation.x += 0.01;
//   cube2.rotation.y += 0.01;

//   renderer.render(scene, camera);
// }

import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  30
);

const mycanvas = document.querySelector("canvas.mycanvas");

const renderer = new THREE.WebGLRenderer({ canvas: mycanvas });

renderer.setSize(900, 400);

const geometry = new THREE.BoxGeometry(1, 1, 1);
const material = new THREE.MeshBasicMaterial({ color: 0x0000ff });

const cube = new THREE.Mesh(geometry, material);

scene.add(cube);
let control = new OrbitControls(camera2, canvas2);
control.enableDamping = true;
control.autoRotate = true;
camera.position.z = 5;

renderer.render(scene, camera);

// 2nd

const scene2 = new THREE.Scene();

const camera2 = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  500
);

const canvas2 = document.querySelector("canvas.canvas2");
const renderer2 = new THREE.WebGLRenderer({ canvas: canvas2 });

renderer2.setSize(window.innerWidth, window.innerHeight);

const geometry2 = new THREE.BoxGeometry(1, 1, 1);
const material2 = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
const cube2 = new THREE.Mesh(geometry2, material2);

scene2.add(cube2);

camera2.position.z = 5;

renderer2.render(scene2, camera2);
