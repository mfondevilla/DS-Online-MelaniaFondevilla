import pandas as pd
import re

# ============================
# 1. LIMPIEZA DE RAM
# ============================
def clean_ram(df):
    df["Ram"] = df["Ram"].str.replace("GB", "").astype(int)
    return df

# ============================
# 2. LIMPIEZA DE PESO
# ============================
def clean_weight(df):
    df["Weight"] = (
        df["Weight"]
        .astype(str)
        .str.replace("kg", "")
        .str.strip()
    )
    df["Weight"] = pd.to_numeric(df["Weight"], errors="coerce")
    return df

# ============================
# 3. PARSEAR MEMORY
# ============================
def parse_memory(df):
    mem = (
        df["Memory"]
        .astype(str)
        .str.replace("GB", "")
        .str.replace("TB", "000")
    )

    parts = mem.str.split("+", expand=True)

    def extract_capacity(text):
        if text is None or text == "nan":
            return 0
        text = text.strip()
        nums = re.findall(r"\d+", text)
        if not nums:
            return 0
        return int(nums[0])

    df["SSD"] = parts[0].apply(lambda x: extract_capacity(x) if "SSD" in str(x) else 0)
    df["HDD"] = parts[0].apply(lambda x: extract_capacity(x) if "HDD" in str(x) else 0)
    df["Flash"] = parts[0].apply(lambda x: extract_capacity(x) if "Flash" in str(x) else 0)
    df["Hybrid"] = parts[0].apply(lambda x: extract_capacity(x) if "Hybrid" in str(x) else 0)

    if parts.shape[1] > 1:
        df["SSD"] += parts[1].apply(lambda x: extract_capacity(x) if "SSD" in str(x) else 0)
        df["HDD"] += parts[1].apply(lambda x: extract_capacity(x) if "HDD" in str(x) else 0)
        df["Flash"] += parts[1].apply(lambda x: extract_capacity(x) if "Flash" in str(x) else 0)
        df["Hybrid"] += parts[1].apply(lambda x: extract_capacity(x) if "Hybrid" in str(x) else 0)

    return df

# ============================
# 4. PARSEAR CPU
# ============================
def parse_cpu(df):
    df["Cpu_brand"] = df["Cpu"].str.split().str[0]
    df["Cpu_model"] = df["Cpu"].str.extract(r"(i3|i5|i7|i9|Ryzen\s?\d+)")
    return df

# ============================
# 5. PARSEAR GPU
# ============================
def parse_gpu(df):
    df["Gpu_brand"] = df["Gpu"].str.split().str[0]
    return df

# ============================
# 6. PARSEAR SCREEN RESOLUTION
# ============================
def parse_screen_resolution(df):
    df["Touchscreen"] = df["ScreenResolution"].str.contains("Touchscreen").astype(int)
    df["Resolution_X"] = df["ScreenResolution"].str.extract(r"(\d+)x").astype(int)
    df["Resolution_Y"] = df["ScreenResolution"].str.extract(r"x(\d+)").astype(int)
    return df

# ============================
# 7. FUNCIÓN PRINCIPAL
# ============================
def clean_dataset(df):
    df = df.copy()
    # Aplicar funciones de limpieza
    df = clean_ram(df)
    df = clean_weight(df)
    df = parse_memory(df)
    df = parse_cpu(df)
    df = parse_gpu(df)
    df = parse_screen_resolution(df)
    
    # Rellenar NaN en categóricas y convertir a string
    df["Cpu_brand"] = df["Cpu_brand"].fillna("Unknown").astype(str)
    df["Cpu_model"] = df["Cpu_model"].fillna("Unknown").astype(str)
    df["Gpu_brand"] = df["Gpu_brand"].fillna("Unknown").astype(str)
    
    # Columnas finales que queremos conservar
    cols_to_keep = [
        "Ram", "Weight",
        "SSD", "HDD", "Flash", "Hybrid",
        "Resolution_X", "Resolution_Y",
        "Touchscreen",
        "Cpu_brand", "Cpu_model", "Gpu_brand"
    ]

    # Si el target está presente, lo conservamos
    if "Price_in_euros" in df.columns:
        cols_to_keep.append("Price_in_euros")

    # Devolver solo las columnas finales
    return df[cols_to_keep]