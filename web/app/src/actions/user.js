import * as api from './../services/api';
import * as auth from './../services/auth';
import { browserHistory } from 'react-router'


export const loginUser = ({email, password}) => {
  return (dispatch) => {
    dispatch({ type: 'LOGIN_USER_PENDING' });
    api.loginUser({email, password}).then((res)=> {
      auth.setToken(res.id_token);
      dispatch({ type: 'LOGIN_USER_SUCCESS' });
      dispatch({
        type: 'SET_CURRENT_USER',
        id: res.id
      });
      browserHistory.replace(`/user/${res.id}/apps`);
    });
  }
};

export const setCurrentUser = ({userId}) => {
  return (dispatch) => {
    dispatch({
      type: 'SET_CURRENT_USER',
      id: userId
    });
  }
};
