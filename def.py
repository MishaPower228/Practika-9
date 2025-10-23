def comfort_advice(temp_c: float, humidity: float) -> str:
    if not (0 <= humidity <= 100):
        return "Помилка: вологість має бути в діапазоні 0–100%."

    if 20 <= temp_c <= 24 and 40 <= humidity <= 60:
        return "Комфортно ✅ Провітрювати не обов'язково."

    tips = []

    # Температура
    if temp_c < 20:
        tips.append("Трохи прохолодно — підвищіть температуру або одягніться тепліше.")
    elif temp_c > 24:
        tips.append("Занадто тепло — зменште нагрів або увімкніть кондиціонер.")

    # Вологість
    if humidity < 40:
        tips.append("Сухо — подумайте про зволоження повітря.")
    elif humidity > 60:
        tips.append("Висока вологість — провітріть або використайте осушувач.")

    return " ".join(tips)

def main():
    try:
        t = float(input("Введіть температуру, °C: ").strip())
        h = float(input("Введіть вологість, %: ").strip())
    except ValueError:
        print("Помилка вводу: введіть числа")
        return

    print(comfort_advice(t, h))

if __name__ == "__main__":
    main()
#Додати щось потрібне для проекту
