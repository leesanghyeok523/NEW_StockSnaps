import { defineStore } from 'pinia';
import axios from 'axios';

export const useSavingsStore = defineStore('savings', {
  state: () => ({
    savings: [], // 초기 상태
  }),
  actions: {
    async fetchSavingsData() {
      try {
        const token = localStorage.getItem('accessToken');
        if (!token) throw new Error('로그인이 필요합니다.');

        const response = await axios.get('http://127.0.0.1:8000/api/core/actions/savings-products/', {
          headers: { Authorization: `Token ${token}` },
        });

        this.savings = Array.isArray(response.data) ? response.data : [];
        console.log('저축 상품 데이터 로드 성공:', this.savings);
      } catch (error) {
        console.error('저축 상품 데이터를 가져오는 데 실패했습니다:', error);
        throw new Error('저축 상품 데이터를 가져오는 데 실패했습니다.');
      }
    },
  },
});
