"use client";
import React, { useState } from "react";
import { Sidebar, SidebarBody, SidebarLink } from "../ui/sidebar";
import {
  IconArrowLeft,
  IconBrandTabler,
  IconSettings,
  IconUserBolt,
} from "@tabler/icons-react";
import Link from "next/link";
import { motion } from "framer-motion";
import { cn } from "../lib/utils";
import { DarkMode } from "../ui/darkMode";
import { AdminUserList } from "../pages/admin/admin-user-list";
import css from "styled-jsx/css";

export function SidebarDemo() {
  const [open, setOpen] = useState(false);

  const links = [
    {
      label: "Dashboard",
      href: "#",
      icon: (
        <IconBrandTabler className="text-green-600 dark:text-green-600 h-8 w-10 flex-shrink-0" />
      ),
    },
    {
      label: "Profile",
      href: "#",
      icon: (
        <IconUserBolt className="text-green-600 dark:text-green-600 h-8 w-10 flex-shrink-0" />
      ),
    },
    {
      label: "User",
      href: "#",
      icon: (
        <IconSettings className="text-green-600 dark:text-green-600 h-8 w-10 flex-shrink-0" />
      ),
      submenu: [
        { label: "List Users", href: "#", icon: null },
        { label: "Average Carbon Footprint", href: "#", icon: null },
      ],
    },
    {
      label: "Logout",
      href: "#",
      icon: (
        <IconArrowLeft className="text-green-600 dark:text-green-600 h-8 w-10 flex-shrink-0" />
      ),
    },
  ];

  const [profileOpen, setProfileOpen] = useState(false);
  const [userOpen, setUserOpen] = useState(false);

  const handleProfileClick = () => {
    setProfileOpen(!profileOpen);
    setUserOpen(false); // Close user submenu if open
  };

  const handleUserClick = () => {
    setUserOpen(!userOpen);
    setProfileOpen(false); // Close profile submenu if open
  };

  const handleSubMenuClick = () => {
    setProfileOpen(false); // Close profile submenu on any submenu click
    setUserOpen(false); // Close user submenu on any submenu click
  };

  return (
    <div
      className={cn(
        "rounded-md flex flex-col md:flex-row w-screen bg-gray-100 dark:bg-neutral-800 flex-1 max-w-8xl mx-auto border border-neutral-200 dark:border-black overflow-hidden",
        "h-[100vh]"
      )}
    >
      <Sidebar open={open} setOpen={setOpen} className="w-96 text-green-600">
        {" "}
        <SidebarBody
          className={cn(
            "justify-between gap-10 text-green-600",
            "border-2 border-black rounded-lg dark:border-neutral-700"
          )}
        >
          <div className="flex flex-col flex-1 overflow-y-auto overflow-x-hidden ">
            {open ? <Logo /> : <LogoIcon />}
            <div className="mt-8 flex flex-col gap-2 ">
              {links.map((link, idx) =>
                link.submenu ? (
                  <div key={idx}>
                    <SidebarLink
                      link={{
                        label: link.label,
                        href: link.href,
                        icon: link.icon,
                      }}
                      onClick={
                        link.label === "Profile"
                          ? handleProfileClick
                          : handleUserClick
                      }
                    />
                    {((profileOpen && link.label === "Profile") ||
                      (userOpen && link.label === "User")) &&
                      link.submenu.map((subLink, subIdx) => (
                        <SidebarLink
                          key={subIdx}
                          link={subLink}
                          className="ml-6 "
                          onClick={handleSubMenuClick}
                        />
                      ))}
                  </div>
                ) : (
                  <SidebarLink key={idx} link={link} />
                )
              )}
            </div>
          </div>

          {open && (
            <div className="mt-4 p-4">
              <DarkMode />
            </div>
          )}
        </SidebarBody>
      </Sidebar>
      <Dashboard />
    </div>
  );
}

export const Logo = () => {
  return (
    <Link
      href="#"
      className="font-normal flex justify-center items-center text-sm text-black py-1 relative z-20 w-full"
    >
      <motion.span
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        className="font-bold text-2xl text-green-600 dark:text-white text-center whitespace-pre"
      >
        EcoLife
      </motion.span>
    </Link>
  );
};

export const LogoIcon = () => {
  return (
    <Link
      href="#"
      className="font-normal flex space-x-2 items-center text-sm text-black py-1 relative z-20"
    ></Link>
  );
};

const Dashboard = () => {
  return (
    <div className="flex flex-1">
      <div className="p-2 md:p-10 rounded-tl-2xl border-2 border-black dark:border-neutral-700 bg-white dark:bg-neutral-900 flex flex-col gap-2 flex-1 w-full h-full">
        <AdminUserList />
      </div>
    </div>
  );
};
