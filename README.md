# FRIDAY — Personal AI Assistant

> A personal AI assistant project built incrementally and continuously evolving toward an advanced, Iron Man-inspired intelligent assistant.

FRIDAY is my long-term personal AI assistant project.

The goal is to progressively build an assistant that can understand natural language, remember information, use tools, interact with computers and devices, and eventually perform complex tasks with minimal user intervention.

This project is being developed step by step, with each version introducing a new capability and improving the underlying architecture.

---

## 🚀 Current Version

**FRIDAY v0.4 — Persistent Memory System**

FRIDAY currently runs as a Python command-line assistant.

The v0.4 architecture introduces a basic persistent memory system that allows FRIDAY to:

- Store information
- Recall stored information
- Forget stored information
- Preserve memories after restarting the program

FRIDAY uses a local JSON file to store memories, while the memory logic is separated into its own `memory.py` module.

The current memory system uses a simple key-value structure. This provides the foundation for developing more advanced and intelligent memory systems in future versions.

---

## ✨ Current Features

FRIDAY v0.4 can:

- Greet the user
- Understand different forms of basic commands
- Clean and normalize user input
- Recognize user intent
- Tell the current time
- Tell the current date
- Respond with the user's name
- Identify itself as FRIDAY
- Respond to basic conversations
- Display available capabilities
- Store information in persistent memory
- Recall previously stored information
- Forget stored information
- - Preserve stored memories after restarting FRIDAY
- Shut down when requested

### 🧠 Memory Examples

```text
remember favorite color is blue

FRIDAY: I'll remember that.
You: what do you remember about favorite color

FRIDAY: favorite color is blue.
You: forget favorite color

FRIDAY: I have forgotten that.