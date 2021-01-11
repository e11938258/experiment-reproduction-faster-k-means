def guardValidRunner(runnerName):
    if runnerName == "NONE":
        raise Exception("Set your name in RESULTS_RUNNER_NAME variable!")