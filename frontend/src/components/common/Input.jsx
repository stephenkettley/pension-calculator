function Input({
    label,
    name,
    type = "text",
    ...props
  }) {
    return (
      <div className="flex flex-col gap-2">
        <label
          htmlFor={name}
          className="text-sm font-semibold text-slate-700"
        >
          {label}
        </label>
  
        <input
          id={name}
          name={name}
          type={type}
          className="
            w-full
            rounded-xl
            border
            border-slate-300
            bg-white/80
            px-4
            py-3
            text-base
            text-slate-900
            placeholder:text-slate-400
            shadow-sm
            transition-all
            duration-200
            outline-none
            focus:border-blue-500
            focus:ring-4
            focus:ring-blue-200
          "
          {...props}
        />
      </div>
    );
  }
  
  export default Input;