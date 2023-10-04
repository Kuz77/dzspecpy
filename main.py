import json
from datetime import datetime


def save_notes(notes):
    with open("notes.json", "w") as f:
        json.dump(notes, f)


def load_notes():
    try:
        with open("notes.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def create_note():
    note_id = input("Введите идентификатор заметки: ")
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {"id": note_id, "title": title, "body": body, "timestamp": timestamp}


def display_notes(notes):
    if notes:
        print("Список заметок:")
        for note in notes:
            print(f"Идентификатор: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['body']}")
            print(f"Дата/Время: {note['timestamp']}")
            print()
    else:
        print("Заметок нет")


def edit_note(notes):
    note_id = input("Введите идентификатор заметки для редактирования: ")
    for note in notes:
        if note["id"] == note_id:
            note["title"] = input("Введите новый заголовок заметки: ")
            note["body"] = input("Введите новый текст заметки: ")
            note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Заметка успешно отредактирована")
            return
    print("Заметка с таким идентификатором не найдена")


def delete_note(notes):
    note_id = input("Введите идентификатор заметки для удаления: ")
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            print("Заметка успешно удалена")
            return
    print("Заметка с таким идентификатором не найдена")


def main():
    notes = load_notes()

    while True:
        print("Выберите действие:")
        print("1. Вывести список заметок")
        print("2. Создать новую заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")

        choice = input()

        if choice == "1":
            display_notes(notes)
        elif choice == "2":
            notes.append(create_note())
            save_notes(notes)
            print("Заметка успешно создана")
        elif choice == "3":
            edit_note(notes)
            save_notes(notes)
        elif choice == "4":
            delete_note(notes)
            save_notes(notes)
        elif choice == "5":
            break
        else:
            print("Некорректный ввод, попробуйте снова")


if __name__ == "__main__":
    main()