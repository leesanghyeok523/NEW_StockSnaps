import { defineStore } from 'pinia';
import axios from 'axios';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isAuthenticated: !!localStorage.getItem('accessToken'),
    accessToken: localStorage.getItem('accessToken') || null,
  }),
  actions: {
    async login(username, password) {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/auth/login/', {
          username,
          password,
        });

        const { key } = response.data;
        this.accessToken = key;
        localStorage.setItem('accessToken', key);
        this.isAuthenticated = true;

        console.log('로그인 성공:', response.data);
      } catch (error) {
        console.error('로그인 실패:', error.response?.data || error.message);
        throw new Error('로그인 실패');
      }
    },
    async logout() {
      try {
        if (!this.accessToken) {
          throw new Error('로그아웃 실패: 토큰이 없습니다.');
        }

        // 로그아웃 요청
        const response = await axios.post(
          'http://127.0.0.1:8000/api/auth/logout/',
          null,
          {
            headers: {
              Authorization: `Token ${this.accessToken}`, // 올바른 토큰 형식 확인
            },
          }
        );

        console.log('로그아웃 성공:', response.data);
        this.clearSession();
      } catch (error) {
        if (error.response?.status === 401) {
          console.error('로그아웃 실패: 유효하지 않은 토큰. 세션을 초기화합니다.');
          this.clearSession(); // 토큰이 유효하지 않을 경우 세션만 초기화
        } else {
          console.error('로그아웃 실패:', error.response?.data || error.message);
          throw new Error('로그아웃 실패');
        }
      }
    },
    clearSession() {
      this.isAuthenticated = false;
      this.accessToken = null;
      localStorage.removeItem('accessToken');
    },
  },
});
