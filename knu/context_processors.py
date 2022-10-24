
from .models import Scenario, Eval

def get_main_scenarios_context(request):
    scenariolist = Scenario.objects.all()
    return {
        'main_scenarios': scenariolist
    }

def get_eval_context(request):
    evallist = Eval.objects.all()
    return {
        'evals': evallist
    }