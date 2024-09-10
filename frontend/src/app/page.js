"use client";

import { GoogleOAuthProvider } from "@react-oauth/google";
import { SidebarDemoUser } from "@/components/user/SidebarDemo-User";
import SignUp from "@/pages/auth/sign-up";

export default function Home() {
  return (
    <GoogleOAuthProvider clientId="YOUR_GOOGLE_CLIENT_ID">
      <SignUp/>
    </GoogleOAuthProvider>
  );
}
