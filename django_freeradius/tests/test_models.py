import os
from unittest import skipIf

from django.test import TestCase

from django_freeradius.models import (
    Nas, RadiusAccounting, RadiusBatch, RadiusCheck, RadiusGroupCheck, RadiusGroupReply, RadiusPostAuth,
    RadiusProfile, RadiusReply, RadiusUserGroup, RadiusUserProfile,
)

from .base.test_models import (
    BaseTestNas, BaseTestRadiusAccounting, BaseTestRadiusBatch, BaseTestRadiusCheck,
    BaseTestRadiusGroupCheck, BaseTestRadiusGroupReply, BaseTestRadiusPostAuth, BaseTestRadiusProfile,
    BaseTestRadiusReply, BaseTestRadiusUserGroup, BaseTestRadiusUserProfile,
)


@skipIf(os.environ.get('SAMPLE_APP', False), 'Running tests on SAMPLE_APP')
class TestNas(BaseTestNas, TestCase):
    nas_model = Nas


@skipIf(os.environ.get('SAMPLE_APP', False), 'Running tests on SAMPLE_APP')
class TestRadiusAccounting(BaseTestRadiusAccounting, TestCase):
    radius_accounting_model = RadiusAccounting


@skipIf(os.environ.get('SAMPLE_APP', False), 'Running tests on SAMPLE_APP')
class TestRadiusCheck(BaseTestRadiusCheck, TestCase):
    radius_check_model = RadiusCheck


@skipIf(os.environ.get('SAMPLE_APP', False), 'Running tests on SAMPLE_APP')
class TestRadiusReply(BaseTestRadiusReply, TestCase):
    radius_reply_model = RadiusReply


@skipIf(os.environ.get('SAMPLE_APP', False), 'Running tests on SAMPLE_APP')
class TestRadiusGroupReply(BaseTestRadiusGroupReply, TestCase):
    radius_groupreply_model = RadiusGroupReply


@skipIf(os.environ.get('SAMPLE_APP', False), 'Running tests on SAMPLE_APP')
class TestRadiusGroupCheck(BaseTestRadiusGroupCheck, TestCase):
    radius_groupcheck_model = RadiusGroupCheck


@skipIf(os.environ.get('SAMPLE_APP', False), 'Running tests on SAMPLE_APP')
class TestRadiusUserGroup(BaseTestRadiusUserGroup, TestCase):
    radius_usergroup_model = RadiusUserGroup


@skipIf(os.environ.get('SAMPLE_APP', False), 'Running tests on SAMPLE_APP')
class TestRadiusPostAuth(BaseTestRadiusPostAuth, TestCase):
    radius_postauth_model = RadiusPostAuth


@skipIf(os.environ.get('SAMPLE_APP', False), 'Running tests on SAMPLE_APP')
class TestRadiusBatch(BaseTestRadiusBatch, TestCase):
    radius_batch_model = RadiusBatch


@skipIf(os.environ.get('SAMPLE_APP', False), 'Running tests on SAMPLE_APP')
class TestRadiusProfile(BaseTestRadiusProfile, TestCase):
    radius_profile_model = RadiusProfile


@skipIf(os.environ.get('SAMPLE_APP', False), 'Running tests on SAMPLE_APP')
class TestRadiusUserProfile(BaseTestRadiusUserProfile, TestCase):
    radius_profile_model = RadiusProfile
    radius_userprofile_model = RadiusUserProfile
    radius_check_model = RadiusCheck
