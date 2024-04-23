from NoteManager import NoteManager

def main():
    note_manager = NoteManager()
    while True:
        print("\nМеню:")
        print("1. Создать заметку")
        print("2. Просмотреть заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            note_manager.create_note(title, body)
            print("Заметка успешно создана.")
        elif choice == "2":
            note_manager.read_notes()
        elif choice == "3":
            if not note_manager.notes:
                print("Заметок нет.")
            else:
                note_id = int(input("Введите ID заметки, которую хотите отредактировать: "))

                if any(note.id == note_id for note in note_manager.notes):
                    new_title = input("Введите новый заголовок (оставьте пустым, чтобы не изменять): ")
                    new_body = input("Введите новый текст (оставьте пустым, чтобы не изменять): ")
                    if note_manager.edit_note(note_id, new_title, new_body):
                        print("Заметка успешно отредактирована.")
                else:
                    print("Заметка с указанным ID не найдена.")
        elif choice == "4":
            if not note_manager.notes:
                print("Заметок нет.")
            else:
                note_id = int(input("Введите ID заметки, которую хотите удалить: "))
                if note_manager.delete_note(note_id):
                    print("Заметка успешно удалена.")
                else:
                    print("Заметка с указанным ID не найдена.")
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите существующую опцию.")

if __name__ == "__main__":
    main()
