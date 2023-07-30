1. **Exported Variables**: `FLASK_APP`, `FLASK_ENV`, `DATABASE_URI`, `SECRET_KEY`, `WHISPER_API_KEY`, `DOCKER_COMPOSE_FILE`, `GIT_REPO_URL`.

2. **Data Schemas**: `User` (with fields `id`, `username`, `password`, `email`), `Task` (with fields `id`, `task_description`, `status`, `output`, `user_id`).

3. **DOM Element IDs**: `login-form`, `username-input`, `password-input`, `git-clone-input`, `file-upload-input`, `task-input`, `task-output`, `save-output-btn`, `new-task-btn`, `exit-btn`.

4. **Message Names**: `LOGIN_SUCCESS`, `LOGIN_FAILURE`, `GIT_CLONE_SUCCESS`, `GIT_CLONE_FAILURE`, `FILE_UPLOAD_SUCCESS`, `FILE_UPLOAD_FAILURE`, `TASK_INPUT_SUCCESS`, `TASK_INPUT_FAILURE`, `TASK_EXECUTION_SUCCESS`, `TASK_EXECUTION_FAILURE`, `OUTPUT_PRESENTATION_SUCCESS`, `OUTPUT_PRESENTATION_FAILURE`.

5. **Function Names**: `authenticateUser`, `cloneGitRepo`, `uploadFile`, `inputTask`, `manageAIagentTask`, `executeTask`, `presentOutput`, `createAIagent`, `getUser`, `getTask`, `saveOutput`, `startNewTask`, `exitApplication`.