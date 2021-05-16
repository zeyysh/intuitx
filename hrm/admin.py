from django.contrib import admin
import hrm.models as hmodels
from admin_helpers import AdminChangeLinksMixin
from users.admin import BaseModelAdmin


'''
class CompanyAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ('name', 'project_companies_link',)
    changelist_links = ('project_companies', 'company_strategies', 'company_products')
    search_fields = ('name',)
'''


class ProjectAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ('name', 'company_link',)    
    change_links = ('company',)
    changelist_links = ('company_products', 'company_strategies')
    list_filter = ('company',)
    search_fields = ('company__name', 'name')
    autocomplete_fields = ('company',)


class TeamAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ('name', 'project_link', 'team_model_link', 'team_lead_link')
    changelist_links = ('associated_team_positions', 'team_milestones')
    change_links = ('project', 'team_lead', 'team_model')
    autocomplete_fields = ('project', 'team_lead')
    filter_horizontal = ('resources',)
    search_fields = ('project__name',)
    list_filter = ('project', 'project__company')


class ResourceAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ('assigned_candidate_link', 'fulltime_multiple')
    change_links = ('assigned_candidate',)
    changelist_links = ('team_set',)#'resource_time_logs')
    autocomplete_fields = ('assigned_candidate',)
    search_fields = ('assigned_candidate__name',)
    list_filter = ('fulltime_multiple',)# 'team_set')    


class TimeLogAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ('resource__assigned_candidate__name', 'start_time', 'end_time')
    change_links = ('resource',)
    autocomplete_fields = ('resource',)
    search_fields = ('resource__assigned_candidate')
    list_filter = ('created_at', 'resource__assigned_candidate')


class CandidateAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ('user', 'candidate_lead_link')
    list_filter = ('assigned_candidate_resources',)
    changelist_links = ('applied_to_candidate_contract_work_packages', 'candidate_payrolls', 'team_lead_teams', 'assigned_candidate_resources', 'filled_with_candidate_positions', 'assignee_tasks')
    search_fields = ('user__name', 'user__email',)
    change_links = ('candidate_lead',)


class PositionAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ('title', 'associated_team_link', 'filled_with_candidate_link', 'onboarding_link')
    change_links = ('associated_team', 'filled_with_candidate', 'onboarding')
    autocomplete_fields = ('associated_team', 'filled_with_candidate')# 'team_model', 'team_lead')
    search_fields = ('title',)
    list_filter = ('suggested_expired', 'associated_team__project')


class OnboardingAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ('name', 'description', 'onboarding_positions_link')
    changelist_links = ('onboarding_positions',)
    filter_horizontal = ('onboarding_steps',)


class OnboardingStepAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ('name', 'description', )
    changelist_links = ('step_completed_onboarding_steps', 'onboarding_steps_onboardings')
    #change_links = ('onboarding_steps_onboardings',)
    search_fields = ('name', 'description')


class CompletedOnboardingStepAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ('candidate_link', 'step_link', 'completed_at')
    change_links = ('candidate', 'step')
    autocomplete_fields = ('candidate', 'step')


class MilestoneAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    pass


class MilestoneEntryAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ('title', 'assignee_link', 'due_date', 'quarter')
    change_links = ('assignee', 'milestone', 'milestone__team', 'milestone_tier')
    autocomplete_fields = ('assignee', 'milestone', 'milestone_tier')
    search_fields = ('title', 'assignee')
    list_filter = ('milestone__team__project__name', 'milestone__team__project__company', 'milestone_tier')


class MilestoneTierAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ('name',)
    changelist_links = ('milestone_tier_milestone', 'parent_tiers')
    autocomplete_fields = ('subtier',)
    search_fields = ('name',)


class TaskAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ('name', 'assignee_link', 'milestone_link')
    change_links = ('assignee', 'milestone')
    list_filter = ('milestone',)


class HRKpiAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    pass


class RewardAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    pass


class BudgetAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    pass


class CandidateSubmissionAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    pass


class PolicyAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    pass


class PayrollAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ('candidate_link', 'amount', 'monthly_date')
    changelist_links = ('payroll_expenses',)
    change_links = ('candidate',)
    list_filter = ('monthly_date',)
    autocomplete_fields = ('candidate',)
    search_fields = ('candidate__name',)


class ContractWorkPackageAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ('name', 'description', 'applied_to_candidate_link')
    changelist_links = ('contract_work_package_contract_work_prices',)
    change_links = ('applied_to_candidate',)
    list_filter = ('applied_to_candidate__user__name',)
    autocomplete_fields = ('applied_to_candidate',)
    search_fields = ('name', 'applied_to_candidate__name')


class ContractWorkPriceAdmin(AdminChangeLinksMixin, BaseModelAdmin):
    list_display = ('name', 'description', 'contract_work_package_link', 'price')
    change_links = ('contract_work_package',)
    list_filter = ('contract_work_package',)
    autocomplete_fields = ('contract_work_package',)
    search_fields = ('name', 'description')


admin.site.register(hmodels.Project, ProjectAdmin)
admin.site.register(hmodels.Team, TeamAdmin)
admin.site.register(hmodels.Resource, ResourceAdmin)
admin.site.register(hmodels.Candidate, CandidateAdmin)
admin.site.register(hmodels.Position, PositionAdmin)
admin.site.register(hmodels.Milestone, MilestoneAdmin)
#admin.site.register(hmodels.MilestoneEntry, MilestoneEntryAdmin)
admin.site.register(hmodels.MilestoneTier, MilestoneTierAdmin)
admin.site.register(hmodels.Task, TaskAdmin)
admin.site.register(hmodels.HRKpi, HRKpiAdmin)
admin.site.register(hmodels.Reward, RewardAdmin)
admin.site.register(hmodels.Budget, BudgetAdmin)
admin.site.register(hmodels.CandidateSubmission, CandidateSubmissionAdmin)
admin.site.register(hmodels.Policy, PolicyAdmin)
admin.site.register(hmodels.Payroll, PayrollAdmin)
admin.site.register(hmodels.ContractWorkPackage, ContractWorkPackageAdmin)
admin.site.register(hmodels.ContractWorkPrice, ContractWorkPriceAdmin)
admin.site.register(hmodels.Onboarding, OnboardingAdmin)
admin.site.register(hmodels.OnboardingStep, OnboardingStepAdmin)
admin.site.register(hmodels.CompletedOnboardingStep, CompletedOnboardingStepAdmin)