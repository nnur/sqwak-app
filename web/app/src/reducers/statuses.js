const defaultStatuses = {
  isFetchingApps: true,
  isLoginPending: false,
  areFilesUploading: false
};

const statuses = (state = defaultStatuses, action) => {
  switch (action.type) {

    case 'FETCH_APPS_PENDING': {
      return Object.assign({}, state, {
        isFetchingApps: true
      });
    }

    case 'FETCH_APPS_RESOLVED': {
      return Object.assign({}, state, {
        isFetchingApps: false
      });
    }

    case 'FILES_UPLOADING': {
      return Object.assign({}, state, {
        areFilesUploading: true
      });
    }

    case 'FILES_UPLOADED': {
      return Object.assign({}, state, {
        areFilesUploading: false
      });
    }

    case 'LOGIN_USER_PENDING': {
      return Object.assign({}, state, {
        isLoginPending: true
      });
    }

    case 'LOGIN_USER_SUCCESS': {
      return Object.assign({}, state, {
        isLoginPending: false
      });
    }

    default:
      return state
  }
}

export default statuses