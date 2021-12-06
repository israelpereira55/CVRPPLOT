from absl import app, flags
FLAGS = flags.FLAGS

flags.DEFINE_string("instance", None, help="Path to the instance file")
flags.DEFINE_string("solution", None, 'Run with a toy example instead of an instance.')

from vrp import CVRP, reader, plot

def main(argv):

    if FLAGS.instance is None or FLAGS.solution is None:
        print("Please describe the CVRP instace and solution filenames.\nAborting...")
        exit(1)

    cvrp = reader.create_cvrp_by_instance(FLAGS.instance, tsp95_standard=True)
    cvrp.print_instance()

    solution = reader.create_cvrp_solution_by_file(FLAGS.solution, add_one=False)
    solution.print_solution()

    cost = solution.calculate_cost(cvrp)
    if solution.cost != cost:
        user_input = input(f"\nDifferent Cost!\nInstance={solution.cost} vs Real={cost}\n\nWanna continue? (yes/no)\n> ")
        if user_input != 'yes':
            print("Aborting...")
            exit(1)

    plot.plot_cvrp_solution(cvrp, solution, show_numbers=True)


if __name__ == "__main__":
    app.run(main)
