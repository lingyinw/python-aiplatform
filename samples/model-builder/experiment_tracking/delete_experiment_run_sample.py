# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#  [START aiplatform_sdk_delete_experiment_run_sample]
from typing import Union

from google.cloud import aiplatform


def delete_experiment_run_sample(
    run_name: str,
    experiment: Union[str, aiplatform.Experiment],
    project: str,
    location: str,
    delete_backing_tensorboard_run: bool = False,
):
    experiment_run = aiplatform.ExperimentRun(
        run_name=run_name, experiment=experiment, project=project, location=location
    )

    experiment_run.delete(delete_backing_tensorboard_run=delete_backing_tensorboard_run)


#  [END aiplatform_sdk_delete_experiment_run_sample]
