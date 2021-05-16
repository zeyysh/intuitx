# Generated by Django 3.1.3 on 2021-04-12 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('hrm', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='timelog',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrm_company_timelog', to='users.company'),
        ),
        migrations.AddField(
            model_name='timelog',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='timelog',
            name='resource',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resource_time_logs', to='hrm.resource'),
        ),
        migrations.AddField(
            model_name='team',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrm_company_team', to='users.company'),
        ),
        migrations.AddField(
            model_name='team',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='team',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_project', to='hrm.project'),
        ),
        migrations.AddField(
            model_name='team',
            name='resources',
            field=models.ManyToManyField(to='hrm.Resource'),
        ),
        migrations.AddField(
            model_name='team',
            name='team_lead',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_lead_teams', to='hrm.candidate'),
        ),
        migrations.AddField(
            model_name='task',
            name='assignee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignee_tasks', to='hrm.candidate'),
        ),
        migrations.AddField(
            model_name='task',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrm_company_task', to='users.company'),
        ),
        migrations.AddField(
            model_name='task',
            name='milestone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='milestone_tasks', to='hrm.milestone'),
        ),
        migrations.AddField(
            model_name='task',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='reward',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrm_company_reward', to='users.company'),
        ),
        migrations.AddField(
            model_name='reward',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='resource',
            name='assigned_candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_candidate_resources', to='hrm.candidate'),
        ),
        migrations.AddField(
            model_name='resource',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrm_company_resource', to='users.company'),
        ),
        migrations.AddField(
            model_name='resource',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='project',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_companies', to='users.company'),
        ),
        migrations.AddField(
            model_name='project',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='position',
            name='associated_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='associated_team_positions', to='hrm.team'),
        ),
        migrations.AddField(
            model_name='position',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrm_company_position', to='users.company'),
        ),
        migrations.AddField(
            model_name='position',
            name='filled_with_candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filled_with_candidate_positions', to='hrm.candidate'),
        ),
        migrations.AddField(
            model_name='position',
            name='onboarding',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='onboarding_positions', to='hrm.onboarding'),
        ),
        migrations.AddField(
            model_name='position',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='policy',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrm_company_policy', to='users.company'),
        ),
        migrations.AddField(
            model_name='policy',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='payroll',
            name='candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidate_payrolls', to='hrm.candidate'),
        ),
        migrations.AddField(
            model_name='payroll',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrm_company_payroll', to='users.company'),
        ),
        migrations.AddField(
            model_name='payroll',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='onboardingstep',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrm_company_onboardingstep', to='users.company'),
        ),
        migrations.AddField(
            model_name='onboardingstep',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='onboarding',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrm_company_onboarding', to='users.company'),
        ),
        migrations.AddField(
            model_name='onboarding',
            name='onboarding_steps',
            field=models.ManyToManyField(related_name='onboarding_steps_onboardings', to='hrm.OnboardingStep'),
        ),
        migrations.AddField(
            model_name='onboarding',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='milestonetier',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrm_company_milestonetier', to='users.company'),
        ),
        migrations.AddField(
            model_name='milestonetier',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='milestonetier',
            name='subtier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_tier', to='hrm.milestonetier'),
        ),
        migrations.AddField(
            model_name='milestoneentry',
            name='assignee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignee_milestone_entries', to='hrm.candidate'),
        ),
        migrations.AddField(
            model_name='milestoneentry',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrm_company_milestoneentry', to='users.company'),
        ),
        migrations.AddField(
            model_name='milestoneentry',
            name='milestone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='milestone_milestone_entries', to='hrm.milestone'),
        ),
        migrations.AddField(
            model_name='milestoneentry',
            name='milestone_tier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='milestone_tier_milestones', to='hrm.milestonetier'),
        ),
        migrations.AddField(
            model_name='milestoneentry',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='milestone',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrm_company_milestone', to='users.company'),
        ),
        migrations.AddField(
            model_name='milestone',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='milestone',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_milestones', to='hrm.team'),
        ),
        migrations.AddField(
            model_name='hrkpi',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrm_company_hrkpi', to='users.company'),
        ),
        migrations.AddField(
            model_name='hrkpi',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='contractworkprice',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrm_company_contractworkprice', to='users.company'),
        ),
        migrations.AddField(
            model_name='contractworkprice',
            name='contract_work_package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contract_work_package_contract_work_prices', to='hrm.contractworkpackage'),
        ),
        migrations.AddField(
            model_name='contractworkprice',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='contractworkpackage',
            name='applied_to_candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applied_to_candidate_contract_work_packages', to='hrm.candidate'),
        ),
        migrations.AddField(
            model_name='contractworkpackage',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrm_company_contractworkpackage', to='users.company'),
        ),
        migrations.AddField(
            model_name='contractworkpackage',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='completedonboardingstep',
            name='candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidate_completed_onboarding_steps', to='hrm.candidate'),
        ),
        migrations.AddField(
            model_name='completedonboardingstep',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrm_company_completedonboardingstep', to='users.company'),
        ),
        migrations.AddField(
            model_name='completedonboardingstep',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='completedonboardingstep',
            name='step',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='step_completed_onboarding_steps', to='hrm.onboardingstep'),
        ),
        migrations.AddField(
            model_name='candidatesubmission',
            name='candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidate_resume', to='hrm.candidate'),
        ),
        migrations.AddField(
            model_name='candidatesubmission',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrm_company_candidatesubmission', to='users.company'),
        ),
        migrations.AddField(
            model_name='candidatesubmission',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrm_company_candidate', to='users.company'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidate_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='budget',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrm_company_budget', to='users.company'),
        ),
        migrations.AddField(
            model_name='budget',
            name='organizations',
            field=models.ManyToManyField(to='users.Organization'),
        ),
    ]
