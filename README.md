# Gravity Shift

<div align="center">

![Gravity Shift Logo](https://via.placeholder.com/400x200/1a1a2e/eee?text=GRAVITY+SHIFT)

**A 2D Space Survival Platformer with Dynamic Gravity Mechanics**

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/username/gravity-shift)
[![Code Coverage](https://img.shields.io/badge/coverage-85%25-green.svg)](https://github.com/username/gravity-shift)
[![Contributors](https://img.shields.io/badge/contributors-5-orange.svg)](https://github.com/username/gravity-shift/graphs/contributors)

[Play Demo](https://gravity-shift-demo.com) · [Report Bug](https://github.com/username/gravity-shift/issues) · [Request Feature](https://github.com/username/gravity-shift/issues)

</div>

---

## Table of Contents

- [About The Project](#about-the-project)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Game Features](#game-features)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

---

## About The Project

![Screenshot](https://via.placeholder.com/800x400/2d3748/fff?text=Gravity+Shift+Gameplay)

**Gravity Shift** is a 2D space survival platformer set in the year 2187, where Earth has become uninhabitable and humanity's last colony on Titan faces catastrophic failure. Players control Alex Rook, a space engineer trapped in a fractured space station with constantly changing gravitational fields.

### The Story

After the Great Crisis of 2135 devastated Earth, humanity established Titan Prime - a massive colony orbiting Saturn. When an experiment with the QX-9 gravity generator goes wrong, the station fragments into three sections with chaotic gravitational anomalies. With only 45 minutes of oxygen and the sarcastic AI companion DELTA, players must navigate through impossible physics to survive.

### Why This Project?

- **Educational Value**: Demonstrates real physics concepts through gameplay
- **Technical Challenge**: Complex gravity simulation and particle systems
- **Narrative Depth**: Rich sci-fi lore with multiple endings
- **Replayability**: Dynamic physics create unique experiences each playthrough

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Built With

This project leverages Python's robust ecosystem for game development:

### Core Technologies

- **[Python 3.8+](https://python.org)** - Primary programming language
- **[Pygame 2.5.2](https://pygame.org)** - 2D game engine and rendering
- **[PyMunk 6.4.0](http://pymunk.org)** - 2D physics simulation library
- **[NumPy 1.24.3](https://numpy.org)** - Mathematical computations and vectors

### Additional Libraries

- **[pygame-menu 4.4.3](https://pygame-menu.readthedocs.io)** - Menu system and UI components
- **[Pydub 0.25.1](https://pydub.com)** - Audio processing and effects
- **[Pillow 9.5.0](https://pillow.readthedocs.io)** - Image processing and manipulation
- **[PyYAML 6.0](https://pyyaml.org)** - Configuration file management

### Development Tools

- **[pytest](https://pytest.org)** - Testing framework
- **[black](https://black.readthedocs.io)** - Code formatting
- **[flake8](https://flake8.pycqa.org)** - Code linting
- **[mypy](https://mypy.readthedocs.io)** - Static type checking

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Getting Started

Follow these instructions to set up the project locally for development and testing.

### Prerequisites

Ensure you have the following installed on your system:

- **Python 3.8 or higher**
  ```bash
  python --version
  ```
- **Git**
  ```bash
  git --version
  ```
- **pip** (usually comes with Python)
  ```bash
  pip --version
  ```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/username/gravity-shift.git
   cd gravity-shift
   ```

2. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install development dependencies** (optional)
   ```bash
   pip install -r requirements-dev.txt
   ```

5. **Run the game**
   ```bash
   python main.py
   ```

### Alternative Installation Methods

#### Using Poetry
```bash
poetry install
poetry run python main.py
```

#### Using Docker
```bash
docker build -t gravity-shift .
docker run -it gravity-shift
```

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Usage

### Basic Controls

| Action | Key | Description |
|--------|-----|-------------|
| **Move** | `WASD` / `Arrow Keys` | Character movement |
| **EVA Thrusters** | `SPACE` | Activate suit propulsion |
| **Gravity Scanner** | `E` | Analyze local gravity fields |
| **DELTA Console** | `TAB` | Access AI companion |
| **Pause Menu** | `ESC` | Game settings and save |

### Command Line Options

```bash
# Start with debug mode
python main.py --debug

# Skip intro cinematic
python main.py --skip-intro

# Set custom resolution
python main.py --resolution 1920x1080

# Enable profiling
python main.py --profile

# Show help
python main.py --help
```

### Configuration

Game settings can be modified in `config/settings.yaml`:

```yaml
graphics:
  resolution: [1280, 720]
  fullscreen: false
  vsync: true
  particle_limit: 500

audio:
  master_volume: 0.8
  music_volume: 0.6
  sfx_volume: 0.7

gameplay:
  difficulty: normal
  oxygen_time: 45  # minutes
  auto_save: true
```

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Game Features

### 🌌 Dynamic Gravity System
- **Multi-body Physics**: Simultaneous gravitational influence from multiple celestial bodies
- **Real-time Calculations**: Accurate implementation of Newton's law of universal gravitation
- **Variable Fields**: Gravity strength ranges from -2g to +3g across different zones

### 🚀 Three Unique Levels

#### Level 1: Omega District (Titan)
- **Environment**: Urban space station with stable 1.35g gravity
- **Challenges**: Reaper-7 drones and electrical hazards
- **Objective**: Reactivate auxiliary generators

#### Level 2: Cassini Ring (Hyperion)
- **Environment**: Asteroid field with 0.02g chaotic gravity
- **Challenges**: Nitrogen geysers and debris storms
- **Objective**: Collect research data from abandoned stations

#### Level 3: Singularity Core (Enceladus)
- **Environment**: Ice platforms with alternating gravity
- **Challenges**: Melting surfaces and gravitational inversions
- **Objective**: Control or destroy the singularity

### 🤖 DELTA AI Companion
- **Personality**: Sarcastic and pragmatic artificial intelligence
- **Functions**: Oxygen monitoring, threat analysis, and environmental scanning
- **Dialogue System**: Over 200 unique contextual responses

### 🎯 Multiple Endings
- **Destruction Path**: Escape while Titan Prime is lost forever
- **Control Path**: Save colonists but leave the Consortium intact
- **True Ending**: Hidden path requiring collection of all secret logs

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Roadmap

### Current Version (1.0.0)
- [x] Core gravity mechanics implementation
- [x] Three playable levels
- [x] DELTA AI system
- [x] Multiple endings
- [x] Save/load functionality

### Version 1.1.0 (Q2 2024)
- [ ] Additional character customization options
- [ ] Speedrun mode with leaderboards  
- [ ] Advanced graphics settings
- [ ] Controller support
- [ ] Steam Workshop integration

### Version 1.2.0 (Q3 2024)
- [ ] Cooperative multiplayer mode
- [ ] Level editor with community sharing
- [ ] Dynamic weather events
- [ ] Expanded DELTA dialogue system
- [ ] VR compatibility exploration

### Version 2.0.0 (Q4 2024)
- [ ] Mobile port (Android/iOS)
- [ ] Procedurally generated levels
- [ ] Online multiplayer with up to 4 players
- [ ] Competitive game modes
- [ ] Advanced physics simulation

See the [open issues](https://github.com/username/gravity-shift/issues) for a full list of proposed features and known issues.

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Contributing

Contributions make the open source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

### How to Contribute

1. **Fork the Project**
2. **Create your Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Development Guidelines

#### Code Style
- Follow [PEP 8](https://pep8.org/) Python style guidelines
- Use [Black](https://black.readthedocs.io/) for code formatting
- Maximum line length: 88 characters
- Use type hints for all function parameters and return values

#### Testing
- Write unit tests for all new features
- Maintain minimum 80% code coverage
- Run the full test suite before submitting PRs
- Include integration tests for complex features

#### Documentation
- Update README.md for significant changes
- Document all public functions and classes
- Include docstrings following [Google Style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- Update CHANGELOG.md with your changes

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_gravity_system.py

# Run with verbose output
pytest -v
```

### Code Quality Checks

```bash
# Run linting
flake8 src tests

# Run type checking
mypy src

# Run formatting check
black --check src tests

# Run all quality checks
make check-all
```

<p align="right">(<a href="#top">back to top</a>)</p>

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

### Third-Party Licenses

This project uses several open-source libraries. Their licenses can be found in:
- `licenses/pygame.txt` - Pygame License
- `licenses/pymunk.txt` - PyMunk License  
- `licenses/numpy.txt` - NumPy License

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Contact

### Development Team

- **Juan Villalobos** - Physics & Mathematics - [@juanvilla](https://github.com/juanvilla)
- **Luis Barajas** - QA & Testing - [@luisbarajas](https://github.com/luisbarajas)
- **Valentina Molina** - Art & Audio - [@valentina](https://github.com/valentina)
- **Mayoli Catari** - UI/UX Design - [@mayoli](https://github.com/mayoli)
- **Diego Botina** - Lead Developer - [@diegobotina](https://github.com/diegobotina)

### Project Links

- **Repository**: [https://github.com/username/gravity-shift](https://github.com/username/gravity-shift)
- **Issue Tracker**: [https://github.com/username/gravity-shift/issues](https://github.com/username/gravity-shift/issues)
- **Documentation**: [https://gravity-shift.readthedocs.io](https://gravity-shift.readthedocs.io)
- **Demo**: [https://gravity-shift-demo.com](https://gravity-shift-demo.com)

<p align="right">(<a href="#top">back to top</a>)</p>

---

## Acknowledgments

We'd like to thank the following people and projects that made this game possible:

### Libraries and Frameworks
- [Pygame Community](https://pygame.org) for the excellent 2D game development framework
- [PyMunk Developers](http://pymunk.org) for the powerful 2D physics engine
- [NumPy Team](https://numpy.org) for mathematical computing capabilities

### Inspiration and Resources
- **NASA JPL** for accurate planetary data and orbital mechanics
- **Real Physics Simulation** papers by Dr. Sarah Chen (fictional)
- **Indie Game Developer Community** for tutorials and support
- **Open Source Contributors** who make projects like this possible

### Special Thanks
- **Beta Testers** - Community members who provided valuable feedback
- **Translators** - Volunteers helping with internationalization
- **Content Creators** - YouTubers and streamers showcasing the game
- **Academic Advisors** - Physics professors who validated our calculations

### Assets and Media
- **Music**: [Kevin MacLeod](https://incompetech.com) (Licensed under Creative Commons)
- **Sound Effects**: [Freesound.org](https://freesound.org) community
- **Fonts**: [Google Fonts](https://fonts.google.com) open source typography
- **Icons**: [Feather Icons](https://feathericons.com) by Cole Bemis

### Development Tools
- **Visual Studio Code** - Primary development environment
- **GitKraken** - Git client for version control
- **Trello** - Project management and task tracking
- **Discord** - Team communication and community building

---

<div align="center">

**"Gravity unites us... or destroys us."**

*Made with ❤️ and lots of ☕ by the Gravity Shift Team*

[![Pygame](https://img.shields.io/badge/Powered%20by-Pygame-brightgreen.svg)](https://pygame.org)
[![Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://python.org)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

<p align="right">(<a href="#top">back to top</a>)</p>