"""Command-line interface for TaskCLI."""
import argparse
from tasks import add_task, list_tasks, complete_task, remove_task


def main():
    parser = argparse.ArgumentParser(description="TaskCLI - gerenciador de tarefas simples")
    subparsers = parser.add_subparsers(dest="command")

    add_p = subparsers.add_parser("add", help="Adiciona uma nova tarefa")
    add_p.add_argument("description", type=str, help="Descrição da tarefa")

    subparsers.add_parser("list", help="Lista todas as tarefas")

    done_p = subparsers.add_parser("done", help="Marca uma tarefa como concluída")
    done_p.add_argument("id", type=int, help="ID da tarefa")

    remove_p = subparsers.add_parser("remove", help="Remove uma tarefa")
    remove_p.add_argument("id", type=int, help="ID da tarefa")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
        print(f"Tarefa adicionada: {args.description}")
    elif args.command == "list":
        tasks = list_tasks()
        if not tasks:
            print("Nenhuma tarefa cadastrada.")
        for t in tasks:
            status = "✔" if t["done"] else "✗"
            print(f"[{status}] {t['id']}: {t['description']}")
    elif args.command == "done":
        ok = complete_task(args.id)
        print("Tarefa concluída!" if ok else "Tarefa não encontrada.")
    elif args.command == "remove":
        ok = remove_task(args.id)
        print("Tarefa removida!" if ok else "Tarefa não encontrada.")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()