import express, { Request, Response } from "express";
import { prisma } from "./src/config/db.js";

const app = express();

app.use(express.json());

app.get("/", (_req: Request, res: Response) => {
  res.json({ msg: "Hello from home page" });
});

app.post("/api/user", async (req: Request, res: Response) => {
  const { email, name } = req.body as { email?: string; name?: string };

  if (!email || !name) {
    res.status(400).json({ error: "email and name are required" });
    return;
  }

  // Example placeholder write; adjust to your actual model usage.
  await prisma.user.create({ data: { email, name } });

  res.status(201).json({ message: "User created" });
});

app.post("/api/post", async (req: Request, res: Response) => {
  const { title, content, authorId } = req.body as {
    title: string;
    content?: string;
    authorId?: number;
  };

  const post = await prisma.post.create({
    data: {
      title,
      authorId: 2,
      content,
    },
  });

  return res.status(201).json({ message: "Post created", post: post });
});

app.get("/api/post", async (req: Request, res: Response) => {
  const { skip, take } = req.query as { skip?: number; take?: number };
  const posts = await prisma.post.findMany({
    skip: Number(skip),
    take: Number(take),
  });
  return res.status(200).json(posts);
});

app.listen(7000, () => console.log("Server running at port 7000"));
