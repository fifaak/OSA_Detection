<template>
  <form class="login-form" @submit.prevent="handleSubmit">
    <img src="../assets/S__4423684 1.png" style="/* S__4423684 1 */

position: absolute;
width: 246px;
height: 246px;
left: calc(50% - 246px/2);
top: 52px;

background: url(S__4423684.jpg);
border-radius: 120px;
" alt="">
    <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/f8b3c38ac465a7bc7a71441f87d388fb98da3154f1d74ea3f1e940c5c18ceaf1?apiKey=167f8969fc9e4702b2c941ecb34dd7f8&" class="background-image" alt="" />
    <div class="form">
      <h1 style="font-size: 1rem; text-align: center;color: white;">ยินดีต้อนรับสู่ Good Night </h1>
      <div class="input-wrapper">
        <label for="email" class="visually-hidden">Email</label>
        <input
          type="email"
          id="email"
          v-model="email"
          class="input-field"
          placeholder="Email"
          required
        />
      </div>
      <div class="input-wrapper">
        <label for="password" class="visually-hidden">รหัสผ่าน</label>
        <input
          type="password"
          id="password"
          v-model="password"
          class="input-field"
          placeholder="รหัสผ่าน"
          required
        />
      </div>
      <div class="input-wrapper">
        <button type="submit" class="login-button">เข้าสู่ระบบ</button>
      </div>
    </div>
  </form>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
  name: 'LoginForm',
  emits: ['login'],
  setup(props, { emit }) {
    const email = ref('');
    const password = ref('');
    const router = useRouter();

    const handleSubmit = () => {
      emit('login', { email: email.value, password: password.value });
      // Assuming the login is successful, navigate to the home page
      router.push('/home');
    };

    return {
      email,
      password,
      handleSubmit,
    };
  },
};
</script>

<style scoped>
.form {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 30px 20px;
  border-radius: 20px;
  background: rgba(0, 0, 0, 0.5);
  width: 80%;
  height: auto;
  max-width: 400px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.25);
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.input-wrapper {
  width: 100%;
}

.input-field {
  font-family: Rubik, sans-serif;
  border-radius: 30px;
  border: 2px solid #fff;
  padding: 15px 0px;
  width: 95%;
  background: transparent;
  color: #fff;
  font-size: 16px;
  margin-top: 10px;

  padding-left: 10px; /* Adding padding to align text */
}

.input-field::placeholder {
  color: #ddd;
  padding-left: 10px; /* Adding padding to the placeholder */
}

.login-button {
  margin-top: 20px;
  font-family: Rubik, sans-serif;
  border-radius: 30px;
  background-color: #fff;
  padding: 15px 20px;
  color: #000;
  font-weight: 600;
  text-align: center;
  cursor: pointer;
  border: none;
  width: 100%;
  transition: background-color 0.3s;
}

.login-button:hover {
  background-color: #f0f0f0;
}

.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding-left: 10px;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

.background-image {
  position: absolute;
  inset: 0;
  height: 100%;
  width: 100%;
  object-fit: cover;
  object-position: center;
  z-index: -1;
}
</style>
