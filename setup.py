import pandas as pd
import numpy as np

# Parámetros del nivel
ROWS = 16
COLS = 150

# Crear una matriz llena de -1 (espacio vacío)
level_data = np.full((ROWS, COLS), -1)

# Tile IDs usados según el main.py
TILE_PLATFORM = 1
TILE_PLAYER = 15
TILE_ENEMY = 16
TILE_AMMO_BOX = 17
TILE_GRENADE_BOX = 18
TILE_HEALTH_BOX = 19
TILE_EXIT = 20
TILE_WATER = 10
TILE_DECOR_CABLE = 14
TILE_DECOR_SWITCH = 13

# 1. Primera plataforma y jugador
level_data[12, 2] = TILE_PLATFORM
level_data[11, 2] = TILE_PLAYER

# 2. Segunda y tercera plataformas
level_data[12, 6] = TILE_PLATFORM
level_data[12, 10] = TILE_PLATFORM

# 3. Cables electrificados
level_data[13, 20] = TILE_DECOR_CABLE
level_data[13, 21] = TILE_DECOR_CABLE
level_data[13, 22] = TILE_DECOR_CABLE

# 4. Interruptor
level_data[13, 40] = TILE_DECOR_SWITCH

# 5. Caja de munición
level_data[11, 30] = TILE_AMMO_BOX

# 6. Charcos que ralentizan (simulados como agua)
level_data[13, 50] = TILE_WATER
level_data[13, 51] = TILE_WATER
level_data[13, 52] = TILE_WATER

# 7. Enemigo final
level_data[11, 70] = TILE_ENEMY

# 8. Salida
level_data[13, 140] = TILE_EXIT

# Convertir a DataFrame para guardar
df = pd.DataFrame(level_data.astype(int))

# Guardar como nuevo CSV
output_path = "assets/data/levels/level1_data_UPDATED.csv"
df.to_csv(output_path, index=False, header=False)

output_path