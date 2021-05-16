from django.db import models
from users.models import GeneralModel, User, Organization, Company
#from modeler.models import Modeler


'''
class Company(GeneralModel):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, related_name='organization_companies')
    name = models.TextField(max_length=100)

    def __str__(self):
        return 'Company: ' + self.name
'''


class Project(GeneralModel):
    name = models.TextField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name='project_companies')

    def __str__(self):
        return self.name
    

class Team(GeneralModel):
    name = models.CharField(max_length=80)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, related_name='team_project')
    # team_model = models.ForeignKey("Modeler", on_delete=models.CASCADE, null=True, related_name='team_modeler')
    team_lead = models.ForeignKey('Candidate', on_delete=models.CASCADE, null=True, related_name='team_lead_teams')
    resources = models.ManyToManyField('Resource')

    def __str__(self):
        return self.name


class Resource(GeneralModel):
    fulltime_multiple = models.FloatField()
    assigned_candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE, null=True, related_name='assigned_candidate_resources')

    def __str__(self):
        return self.assigned_candidate.user.name + str(self.fulltime_multiple)


class TimeLog(GeneralModel):
    resource = models.ForeignKey('Resource', on_delete=models.CASCADE, null=True, related_name='resource_time_logs')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.resource.assigned_candidate.name


class Candidate(GeneralModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='candidate_user')
    active = models.BooleanField()
    # set of skills and their rating (linked to Modeler? or directly from manual interview results)

    def __str__(self):
        return self.user.name


class Position(GeneralModel):
    ''' Each Team has an associated Modeler with its Threshold Values; possible Positions are then
    created based on remaining requirements as predicted by the Modeler for the current state of the
    Team (given its Resources>Candidates). Some Positions will get filled with Candidates. Position 
    should contain "job post" information for ads and etc. '''

    title = models.TextField(max_length=400)
    associated_team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, related_name='associated_team_positions')
    suggested_expired = models.BooleanField(default=False)
    filled_with_candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE, null=True, related_name='filled_with_candidate_positions')
    POSITION_TYPE_CHOICES = [
        ('internship', 'Internship'),
        ('full-time', 'Full Time'),
        ('part-time', 'Part Time'),
    ]
    position_type = models.CharField(max_length=12, choices = POSITION_TYPE_CHOICES, default='full-time')
    onboarding = models.ForeignKey('Onboarding', on_delete=models.CASCADE, null=True, related_name="onboarding_positions")

    def __str__(self):
        return self.title


class Onboarding(GeneralModel):
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=250)
    protocol = models.FileField()
    onboarding_steps = models.ManyToManyField('OnboardingStep', related_name='onboarding_steps_onboardings')

    def __str__(self):
        return self.name


class OnboardingStep(GeneralModel):
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class CompletedOnboardingStep(GeneralModel):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True, related_name='candidate_completed_onboarding_steps')
    step = models.ForeignKey('OnboardingStep', on_delete=models.CASCADE, null=True, related_name='step_completed_onboarding_steps')
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.candidate.user.name


class Milestone(GeneralModel):
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, related_name='team_milestones')

    def __str__(self):
        return self.team.name


class MilestoneEntry(GeneralModel):
    year = models.IntegerField()
    quarter = models.IntegerField()
    milestone = models.ForeignKey('Milestone', on_delete=models.CASCADE, null=True, related_name='milestone_milestone_entries')
    assignee = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True, related_name='assignee_milestone_entries')
    title = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    due_date = models.DateField()
    milestone_tier = models.ForeignKey('MilestoneTier', on_delete=models.CASCADE, null=True, related_name='milestone_tier_milestones')
    
    def __str__(self):
        return self.title

    
class MilestoneTier(GeneralModel):
    name = models.TextField(max_length=200)
    subtier = models.ForeignKey('MilestoneTier', on_delete=models.CASCADE, null=True, related_name='parent_tier')
    
    def __str__(self):
        return self.name


class Task(GeneralModel):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    milestone = models.ForeignKey('Milestone', on_delete=models.CASCADE, null=True, related_name='milestone_tasks')
    assignee = models.ForeignKey('Candidate', on_delete=models.CASCADE, null=True, related_name='assignee_tasks')

    def __str__(self):
        return self.name


class HRKpi(GeneralModel):
    pass


class Reward(GeneralModel):
    pass


class Budget(GeneralModel):
    pass
    

class CandidateSubmission(GeneralModel):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True, related_name='candidate_resume')
    

class Policy(GeneralModel):
    pass


class Payroll(GeneralModel):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True, related_name='candidate_payrolls')
    amount = models.FloatField()
    monthly_date = models.DateField()

    def __str__(self):
        return self.candidate.user.name


class ContractWorkPackage(GeneralModel):
    name = models.CharField(max_length=80)
    description = models.TextField()
    applied_to_candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True, related_name='applied_to_candidate_contract_work_packages')

    def __str__(self):
        return self.name


class ContractWorkPrice(GeneralModel):
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=250)
    contract_work_package = models.ForeignKey(ContractWorkPackage, on_delete=models.CASCADE, null=True, related_name='contract_work_package_contract_work_prices')
    price = models.FloatField()
    conditions = models.TextField()

    def __str__(self):
        return self.name
    
