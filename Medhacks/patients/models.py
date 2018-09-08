# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=1000,null=True)
    age = models.DateField(null=True)
	
class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
	
class Contact(models.Model):
	patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
	phonenumber = models.CharField(max_length=11)