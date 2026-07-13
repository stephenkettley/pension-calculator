function Button({
    children,
    type = "button",
    ...props
  }) {
    return (
      <button
        type={type}
        className="
          w-full
          rounded-lg
          px-6
          py-2.5
          text-base
          font-semibold
          text-white
          shadow-lg
          transition-all
          duration-200
          bg-[#31445C]
          hover:bg-[#9BC3D8]
          hover:-translate-y-0.5
          hover:shadow-xl
          active:translate-y-0
          disabled:cursor-not-allowed
          disabled:opacity-50
          mt-4
        "
        {...props}
   
   
   
      >
        {children}
      </button>
    );
  }
  
  export default Button;