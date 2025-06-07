# Guía Detallada de Directorios - Gravity Shift

## 🗂️ **Raíz del Proyecto**

### **Archivos de Configuración Principal**
- **`README.md`**: Documentación principal del proyecto (como la que tienes)
- **`LICENSE`**: Licencia MIT del proyecto
- **`CHANGELOG.md`**: Historial de cambios y versiones
- **`requirements.txt`**: Dependencias principales (pygame, pymunk, numpy, etc.)
- **`requirements-dev.txt`**: Dependencias de desarrollo (pytest, black, flake8)
- **`pyproject.toml`**: Configuración moderna de Python (build system, herramientas)
- **`setup.py`**: Script de instalación del paquete
- **`Dockerfile`**: Containerización para despliegue
- **`.gitignore`**: Archivos que Git debe ignorar
- **`main.py`**: Punto de entrada principal del juego

---

## 🤖 **`.github/`** - Automatización GitHub

### **`workflows/`** - GitHub Actions
- **`ci.yml`**: Integración continua (tests automáticos)
- **`build.yml`**: Construcción automática del juego
- **`release.yml`**: Creación automática de releases

### **`ISSUE_TEMPLATE/`** - Plantillas de Issues
- **`bug_report.md`**: Formulario para reportar bugs
- **`feature_request.md`**: Solicitud de nuevas características
- **`question.md`**: Preguntas generales

### **`pull_request_template.md`** - Plantilla para PRs

---

## 💻 **`src/`** - Código Fuente Principal

### **`game/core/`** - Motor del Juego
- **`engine.py`**: Clase principal del motor, loop principal del juego
- **`game_state.py`**: Manejo de estados (menú, jugando, pausa, game over)
- **`scene_manager.py`**: Transiciones entre escenas/niveles
- **`input_handler.py`**: Procesamiento de teclado, mouse, gamepad
- **`camera.py`**: Sistema de cámara 2D (seguimiento, zoom, shake)
- **`time_manager.py`**: Control de tiempo, delta time, pausas

### **`game/entities/`** - Objetos del Juego

#### **`player.py`** - Personaje Principal
- Clase Alex Rook con movimiento, salud, oxígeno
- Sistema EVA thrusters, animaciones
- Interacciones con el entorno

#### **`enemies/`** - Enemigos
- **`base_enemy.py`**: Clase base para todos los enemigos
- **`reaper_drone.py`**: IA de los drones Reaper-7 (patrullaje, ataque)

#### **`objects/`** - Objetos Interactivos
- **`platform.py`**: Plataformas móviles, destructibles
- **`collectible.py`**: Objetos recolectables (oxígeno, datos)
- **`generator.py`**: Generadores que se pueden activar/desactivar
- **`hazard.py`**: Peligros ambientales (electricidad, geysers)

#### **`particles/`** - Sistemas de Partículas
- **`particle_system.py`**: Motor de partículas general
- **`debris.py`**: Escombros espaciales
- **`geyser.py`**: Geysers de nitrógeno específicos

### **`game/physics/`** - Sistema de Física
- **`gravity_system.py`**: Implementación de gravedad dinámica (-2g a +3g)
- **`collision_handler.py`**: Detección y resolución de colisiones
- **`physics_world.py`**: Integración con PyMunk, mundo físico
- **`gravity_field.py`**: Campos gravitacionales localizados

### **`game/levels/`** - Niveles del Juego
- **`base_level.py`**: Clase base para todos los niveles
- **`omega_district.py`**: Nivel 1 - Distrito urbano en Titan
- **`cassini_ring.py`**: Nivel 2 - Campo de asteroides
- **`singularity_core.py`**: Nivel 3 - Núcleo de singularidad
- **`level_loader.py`**: Cargador de archivos TMX (Tiled maps)

### **`game/ui/`** - Interfaz de Usuario

#### **`menus/`** - Menús del Juego
- **`main_menu.py`**: Menú principal con opciones
- **`pause_menu.py`**: Menú de pausa durante el juego
- **`settings_menu.py`**: Configuraciones (audio, gráficos, controles)
- **`credits_menu.py`**: Créditos del equipo de desarrollo
- **`save_load_menu.py`**: Gestión de partidas guardadas

#### **`hud/`** - HUD Durante el Juego
- **`oxygen_meter.py`**: Medidor de oxígeno (45 minutos límite)
- **`health_bar.py`**: Barra de salud del jugador
- **`gravity_indicator.py`**: Brújula/indicador de gravedad actual
- **`minimap.py`**: Minimapa del nivel actual
- **`delta_console.py`**: Consola de comunicación con DELTA AI

#### **`components/`** - Componentes UI Reutilizables
- **`button.py`**: Botones interactivos
- **`slider.py`**: Controles deslizantes (volumen, brillo)
- **`text_box.py`**: Cajas de texto para entrada
- **`progress_bar.py`**: Barras de progreso genéricas

#### **`dialogue/`** - Sistema de Diálogos
- **`dialogue_system.py`**: Motor de diálogos del juego
- **`delta_ai.py`**: IA DELTA con 200+ respuestas contextuales
- **`cutscene_manager.py`**: Manejo de cinemáticas

### **`game/audio/`** - Sistema de Audio
- **`audio_manager.py`**: Gestor principal de audio
- **`music_player.py`**: Reproductor de música de fondo
- **`sfx_player.py`**: Efectos de sonido
- **`audio_mixer.py`**: Mezclador de canales de audio

### **`game/graphics/`** - Sistema Gráfico
- **`renderer.py`**: Renderizador principal 2D
- **`sprite_manager.py`**: Gestión de sprites y texturas
- **`animation_system.py`**: Sistema de animaciones 2D

#### **`effects/`** - Efectos Visuales
- **`lighting.py`**: Sistema de iluminación 2D
- **`post_processing.py`**: Efectos post-procesamiento
- **`screen_shake.py`**: Efectos de temblor de pantalla

#### **`tilemap/`** - Sistema de Mapas
- **`tile_renderer.py`**: Renderizado de tiles
- **`tilemap_loader.py`**: Cargador de mapas Tiled

### **`game/utils/`** - Utilidades
- **`math_utils.py`**: Funciones matemáticas (vectores, física)
- **`file_utils.py`**: Manejo de archivos y paths
- **`config_loader.py`**: Cargador de configuraciones YAML
- **`save_system.py`**: Sistema de guardado/carga
- **`logger.py`**: Sistema de logging
- **`profiler.py`**: Herramientas de profiling/performance

---

## 🎨 **`assets/`** - Recursos del Juego

### **`sprites/`** - Gráficos 2D

#### **`characters/alex_rook/`** - Personaje Principal
- **`idle.png`**: Animación de reposo
- **`walk_cycle.png`**: Ciclo de caminata (spritesheet)
- **`jump.png`**: Salto y caída
- **`eva_thrust.png`**: Usando propulsores EVA
- **`damaged.png`**: Estados de daño
- **`death.png`**: Animación de muerte

#### **`characters/enemies/`** - Enemigos
- **`reaper_drone/`**: Sprites del drone (idle, patrol, attack, destroyed)
- **`hazards/`**: Peligros ambientales (arcos eléctricos, geysers)

#### **`environments/`** - Entornos de Niveles

**`omega_district/`** - Nivel 1 (Titan)
- **`tileset.png`**: Tiles de estructuras metálicas
- **`background_layers/`**: Capas de fondo para parallax
- **`structures/`**: Generadores, plataformas, terminales
- **`props/`**: Decoración (escombros, tuberías, luces)

**`cassini_ring/`** - Nivel 2 (Hyperion)
- **`asteroid_tileset.png`**: Tiles de asteroides
- **`background_space.png`**: Fondo espacial con estrellas
- **`stations/`**: Estaciones abandonadas de investigación
- **`effects/`**: Campos gravitacionales visuales

**`singularity_core/`** - Nivel 3 (Enceladus)
- **`ice_platforms.png`**: Plataformas de hielo que se derriten
- **`core_chamber.png`**: La cámara del núcleo de singularidad
- **`singularity_effect.png`**: Efectos visuales del agujero negro

#### **`ui/`** - Interfaz de Usuario
- **`hud/`**: Elementos del HUD (medidores, brújula, retrato DELTA)
- **`menus/`**: Fondos y componentes de menús
- **`icons/`**: Iconos de objetos, habilidades, logros
- **`cursors/`**: Cursores personalizados

#### **`effects/`** - Efectos Visuales
- **`particles/`**: Texturas para partículas (chispas, humo, energía)
- **`lighting/`**: Gradientes de luz, efectos de resplandor
- **`transitions/`**: Efectos de transición entre escenas

### **`audio/`** - Audio del Juego

#### **`music/`** - Música de Fondo (OGG)
- **`main_theme.ogg`**: Tema principal del juego
- **`omega_district_ambient.ogg`**: Ambient para Nivel 1
- **`cassini_ring_tension.ogg`**: Música tensa para Nivel 2
- **`singularity_core_dramatic.ogg`**: Música dramática Nivel 3
- **`menu_music.ogg`**: Música de menús
- **`credits_music.ogg`**: Música de créditos

#### **`sfx/`** - Efectos de Sonido (WAV)

**`player/`** - Sonidos del Jugador
- **`footsteps/`**: Pasos en metal (3 variaciones)
- **`eva_thruster.wav`**: Sonido de propulsores
- **`oxygen_warning.wav`**: Alerta de oxígeno bajo
- **`heartbeat_low_oxygen.wav`**: Latidos cuando queda poco oxígeno

**`environment/`** - Sonidos Ambientales
- **`gravity_shift_whoosh.wav`**: Sonido cuando cambia la gravedad
- **`electrical_buzz.wav`**: Arcos eléctricos
- **`nitrogen_geyser.wav`**: Geysers de nitrógeno
- **`ice_crack.wav`**: Hielo agrietándose

**`enemies/`** - Sonidos de Enemigos
- **`reaper_drone_scan.wav`**: Drone escaneando
- **`reaper_drone_attack.wav`**: Drone atacando
- **`drone_propulsion.wav`**: Motores del drone

**`ui/`** - Sonidos de Interfaz
- **`button_hover.wav`**: Hover sobre botones
- **`button_click.wav`**: Click de botones
- **`menu_transition.wav`**: Transiciones de menú

**`delta_ai/`** - Sonidos de DELTA
- **`delta_startup.wav`**: DELTA iniciándose
- **`delta_alert.wav`**: DELTA alertando de peligro
- **`delta_analysis.wav`**: DELTA analizando datos

#### **`voice/`** - Audio de Voz (OGG)
- **`delta_dialogue/`**: Líneas de voz de DELTA (sarcásticas)
- **`narrator/`**: Narración de cinemáticas

### **`fonts/`** - Tipografías
- **`orbitron_regular.ttf`**: Fuente sci-fi principal
- **`orbitron_bold.ttf`**: Versión bold para títulos
- **`roboto_mono.ttf`**: Fuente monospace para datos técnicos
- **`space_mono.ttf`**: Fuente alternativa temática espacial

### **`shaders/`** - Shaders GLSL
- **`gravity_field.glsl`**: Shader para visualizar campos gravitacionales
- **`lighting.glsl`**: Sistema de iluminación dinámica
- **`particle_system.glsl`**: Optimización GPU para partículas
- **`post_processing.glsl`**: Efectos post-procesamiento

### **`data/`** - Datos del Juego

#### **`levels/`** - Mapas de Niveles (TMX)
- **`omega_district.tmx`**: Mapa del Nivel 1 (formato Tiled)
- **`cassini_ring.tmx`**: Mapa del Nivel 2
- **`singularity_core.tmx`**: Mapa del Nivel 3
- **`tutorial.tmx`**: Nivel tutorial

#### **`dialogue/`** - Diálogos (CSV)
- **`delta_responses.csv`**: 200+ respuestas contextuales de DELTA
- **`cutscene_scripts.csv`**: Guiones de cinemáticas
- **`character_interactions.csv`**: Diálogos entre personajes

#### **`physics/`** - Datos de Física (CSV)
- **`gravity_constants.csv`**: Constantes gravitacionales por zona
- **`material_properties.csv`**: Propiedades físicas de materiales
- **`celestial_bodies.csv`**: Datos de cuerpos celestes (Titan, Hyperion, Enceladus)

#### **`game_data/`** - Datos de Juego (JSON)
- **`achievements.json`**: Definición de logros
- **`collectibles.json`**: Objetos recolectables
- **`enemy_stats.json`**: Estadísticas de enemigos
- **`player_progression.json`**: Sistema de progresión

#### **`localization/`** - Localización
- **`en/`**: Textos en inglés (ui_text.json, dialogue.json, story_text.json)
- **`es/`**: Textos en español
- **`fr/`**: Textos en francés

---

## ⚙️ **`config/`** - Configuraciones

- **`settings.yaml`**: Configuración principal del juego
- **`keybindings.yaml`**: Mapeo de teclas y controles
- **`audio_config.yaml`**: Configuración de audio
- **`graphics_presets.yaml`**: Presets gráficos (bajo, medio, alto)
- **`development.yaml`**: Configuración para desarrollo

---

## 💾 **`saves/`** - Partidas Guardadas

- **`.gitkeep`**: Mantiene el directorio en Git
- **`default_save.json`**: Partida por defecto/nuevo juego

---

## 📝 **`logs/`** - Archivos de Log

- **`.gitkeep`**: Mantiene el directorio en Git
- **`game.log`**: Log principal del juego (errores, debug)

---

## 🧪 **`tests/`** - Suite de Pruebas

### **Pruebas Unitarias**
- **`test_gravity_system.py`**: Tests del sistema de gravedad
- **`test_player_movement.py`**: Tests de movimiento del jugador
- **`test_collision_detection.py`**: Tests de colisiones
- **`test_audio_system.py`**: Tests del sistema de audio
- **`test_save_system.py`**: Tests de guardado/carga
- **`test_level_loading.py`**: Tests de carga de niveles
- **`test_ui_components.py`**: Tests de componentes UI
- **`test_delta_ai.py`**: Tests de la IA DELTA

### **`fixtures/`** - Datos de Prueba
- **`test_levels/`**: Niveles de prueba
- **`test_audio/`**: Audio de prueba
- **`test_data/`**: Datos de configuración de prueba

### **`integration/`** - Pruebas de Integración
- **`test_full_gameplay.py`**: Tests de gameplay completo
- **`test_level_transitions.py`**: Tests de transiciones
- **`test_ending_sequences.py`**: Tests de finales múltiples

---

## 📚 **`docs/`** - Documentación

### **Documentación Principal**
- **`index.md`**: Índice de documentación
- **`installation.md`**: Guía de instalación
- **`gameplay.md`**: Guía de gameplay

### **`development/`** - Documentación Técnica
- **`architecture.md`**: Arquitectura del software
- **`physics_system.md`**: Documentación del sistema de física
- **`ai_system.md`**: Documentación de DELTA AI
- **`audio_implementation.md`**: Implementación de audio
- **`level_design.md`**: Guía de diseño de niveles

### **`api/`** - Documentación API
- **`game_core.md`**: API del núcleo del juego
- **`physics.md`**: API del sistema de física
- **`entities.md`**: API de entidades
- **`ui_system.md`**: API del sistema UI

### **`assets/`** - Guías de Assets
- **`art_guide.md`**: Guía de estilo artístico
- **`audio_guide.md`**: Guía de audio
- **`localization_guide.md`**: Guía de localización

---

## 🛠️ **`tools/`** - Herramientas de Desarrollo

### **`level_editor/`** - Editor de Niveles
- **`level_editor.py`**: Editor visual de niveles
- **`tile_palette.py`**: Paleta de tiles
- **`export_tools.py`**: Herramientas de exportación

### **`asset_processor/`** - Procesador de Assets
- **`sprite_packer.py`**: Empaquetador de sprites
- **`audio_converter.py`**: Conversor de formatos de audio
- **`texture_optimizer.py`**: Optimizador de texturas

### **`build_tools/`** - Herramientas de Build
- **`build_game.py`**: Constructor del juego
- **`package_assets.py`**: Empaquetador de assets
- **`create_installer.py`**: Creador de instaladores

### **`dev_utils/`** - Utilidades de Desarrollo
- **`performance_profiler.py`**: Profiler de rendimiento
- **`memory_analyzer.py`**: Analizador de memoria
- **`debug_overlay.py`**: Overlay de debug en juego

---

## 📜 **`scripts/`** - Scripts de Automatización

- **`setup_dev_env.sh`**: Configuración de entorno de desarrollo
- **`run_tests.sh`**: Ejecutor de pruebas
- **`build_release.sh`**: Constructor de releases
- **`deploy.sh`**: Script de despliegue
- **`update_dependencies.sh`**: Actualizador de dependencias

---

## 📦 **`dist/` y `build/`** - Directorios de Build

- **`dist/`**: Distribuciones finales (ejecutables, instaladores)
- **`build/`**: Archivos temporales de compilación

---

## 🔑 **Archivos Clave por Funcionalidad**

### **Sistema de Gravedad Dinámico**
- `src/game/physics/gravity_system.py`
- `assets/data/physics/gravity_constants.csv`
- `assets/shaders/gravity_field.glsl`

### **IA DELTA**
- `src/game/ui/dialogue/delta_ai.py`
- `assets/data/dialogue/delta_responses.csv`
- `assets/audio/voice/delta_dialogue/`

### **Los 3 Niveles Únicos**
- `src/game/levels/omega_district.py`
- `assets/data/levels/omega_district.tmx`
- `assets/sprites/environments/omega_district/`

### **Sistema de Audio**
- `src/game/audio/audio_manager.py`
- `assets/audio/music/` y `assets/audio/sfx/`
- `config/audio_config.yaml`

Esta estructura está diseñada para ser escalable, mantenible y seguir las mejores prácticas de desarrollo de videojuegos en Python.