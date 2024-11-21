<template>
  <div class="signup-page">
    <div class="signup-container">
      <h1>회원가입</h1>
      <form @submit.prevent="signUp">
        <div class="form-group">
          <label for="username">아이디</label>
          <input id="username" v-model="username" type="text" placeholder="아이디를 입력하세요" required />
        </div>
        <div class="form-group">
          <label for="nickname">닉네임</label>
          <input id="nickname" v-model="nickname" type="text" placeholder="닉네임을 입력하세요" required />
        </div>
        <div class="form-group">
          <label for="email">이메일</label>
          <input id="email" v-model="email" type="email" placeholder="이메일을 입력하세요" required />
        </div>
        <div class="form-group">
          <label for="birthdate">생년월일</label>
          <input id="birthdate" v-model="birthdate" type="date" placeholder="생년월일을 선택하세요" required />
        </div>
        <div class="form-group">
          <label for="password1">비밀번호</label>
          <input id="password1" v-model="password1" type="password" placeholder="비밀번호를 입력하세요" required />
        </div>
        <div class="form-group">
          <label for="password2">비밀번호 확인</label>
          <input id="password2" v-model="password2" type="password" placeholder="비밀번호를 다시 입력하세요" required />
        </div>
        <button type="submit" class="signup-button">회원가입</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref } from 'vue';

export default {
  setup() {
    const username = ref('');
    const nickname = ref('');
    const email = ref('');
    const birthdate = ref('');
    const password1 = ref('');
    const password2 = ref('');

    const signUp = async () => {
      try {
        await axios.post('http://127.0.0.1:8000/api/auth/registration/', {
          username: username.value,
          nickname: nickname.value,
          email: email.value,
          birthdate: birthdate.value,
          password1: password1.value,
          password2: password2.value,
        });
        alert('회원가입 성공!');
        window.location.href = '/login';
      } catch (error) {
        console.error('회원가입 실패:', error.response?.data || error.message);
        alert('회원가입 실패. 다시 시도해주세요.');
      }
    };

    return { username, nickname, email, birthdate, password1, password2, signUp };
  },
};
</script>

<style scoped>
.signup-page {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background: linear-gradient(to right, #6a11cb, #2575fc);
  font-family: "Roboto", sans-serif;
}

.signup-container {
  background: white;
  padding: 40px 50px;
  border-radius: 15px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  text-align: center;
  max-width: 400px;
  width: 100%;
}

h1 {
  font-size: 2rem;
  color: #333;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
  text-align: left;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #555;
}

input {
  width: 100%;
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  outline: none;
}

.signup-button {
  width: 100%;
  padding: 12px 15px;
  font-size: 1rem;
  border: none;
  border-radius: 5px;
  background: linear-gradient(to right, #6a11cb, #2575fc);
  color: white;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.signup-button:hover {
  background: linear-gradient(to right, #5a0eab, #1f5fc8);
}

.back-button {
  margin-top: 10px;
  background-color: #f0f0f0;
  color: #555;
  font-size: 0.9rem;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.back-button:hover {
  background-color: #d9d9d9;
}
</style>
