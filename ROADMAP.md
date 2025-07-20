# 🧭 Firedrill Roadmap

Welcome to the Firedrill roadmap! This document outlines where the project is headed, what features we're exploring, and how the tool may evolve over time. If you're thinking of contributing or just want to see what’s on the horizon, this is the place.

---

## ✅ Core Goals (v1.x)

These are the baseline goals that make Firedrill useful and fun:

- [x] Run GPT-powered incident scenarios from simple YAML
- [x] CLI experience with `make start` and `make start-random`
- [x] Public open source repo
- [x] Lightweight, flexible architecture

---

## 🔭 Next Priorities (v1.1–v1.5)

Features we're actively exploring:

- [ ] Error handling for missing/invalid scenarios
- [ ] CLI output polish (color, timestamping, clearer prompts)
- [ ] Post-scenario recap and optional feedback

---

## 🧠 Future Ideas: Simulation Depth

Possibilities to make Firedrill more lifelike and immersive:

- [ ] Branching scenario paths with multiple outcomes
- [ ] Fake logs/metrics in Datadog-style text chunks
- [ ] GPT-generated teammates (DevOps, PM, etc.)
- [ ] Performance scoring / incident effectiveness feedback
- [ ] “Hardcore” mode with reduced hints and time pressure

---

## 🔌 Infra Awareness (Stretch Goals)

These features would let Firedrill connect to live (safe) environments:

- [ ] Inject read-only alerts from actual dev/staging systems
- [ ] Pull past RCA data into new scenarios
- [ ] Integrate with Datadog, PagerDuty, Prometheus, etc.
- [ ] Support real `kubectl`-driven incidents in isolated sandboxes

---

## 👥 Team Mode (Web UI Concept)

We’re exploring collaborative learning in the future:

- [ ] Web UI for running and editing scenarios
- [ ] Team mode: multiple users simulate a call together
- [ ] Slack-style interface for “incident room” realism
- [ ] Shared scoreboards or heatmaps of practice activity

---

## 🎁 Polish and Delivery

Quality-of-life goals that make Firedrill more usable and portable:

- [ ] Packaged CLI binary via PyInstaller
- [ ] Homebrew formula (`brew install firedrill`)
- [ ] Optional VSCode plugin or shell integration
- [ ] Slackbot or GitHub Action interface

---

## 💡 Got ideas?

Open an issue or email [contact@lukerouker.com](mailto:contact@lukerouker.com) if you’ve got a scenario, feature idea, or just want to chat.

We’re still early — the future is wide open. 🚒
