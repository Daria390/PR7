import data_loader
import task1
import task2
import task3


def main():
    data = data_loader.load_data()

    if data is None:
        return

    task1.run_task1(data)
    task2.run_task2(data)
    task3.run_task3(data)


if __name__ == "__main__":
    main()
